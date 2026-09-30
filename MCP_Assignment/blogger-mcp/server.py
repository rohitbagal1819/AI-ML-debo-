"""
Blogger Publishing Assistant MCP
================================
A small FastMCP server that lets Claude help you write and publish posts on
your Blogger blog.

It contains EXACTLY three MCP primitives (as required by the assignment):

    1 tool      -> publish_blog_post          (action, has side effects)
    1 resource  -> blogger://posts/recent     (read-only data)
    1 prompt    -> create_blog_post           (reusable instruction template)

Flow:  User -> Claude -> this MCP server -> Blogger API -> your Blogger blog

Secrets are NEVER stored in this file. OAuth files and the blog ID are read
from the local `credentials/` folder and from environment variables / `.env`.
"""

import os
from pathlib import Path

import markdown as md
from dotenv import load_dotenv
from fastmcp import FastMCP
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --------------------------------------------------------------------------
# Configuration (no secrets in code)
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

SCOPES = ["https://www.googleapis.com/auth/blogger"]


def _path_from_env(name: str, default: str) -> Path:
    """Read a file path from an environment variable (relative to project)."""
    p = Path(os.getenv(name, default))
    return p if p.is_absolute() else BASE_DIR / p


mcp = FastMCP("Blogger Publishing Assistant")


# --------------------------------------------------------------------------
# Helper functions (plain Python helpers - NOT MCP primitives)
# --------------------------------------------------------------------------
def _get_blog_id() -> str:
    blog_id = os.getenv("BLOGGER_BLOG_ID", "").strip()
    if not blog_id:
        raise RuntimeError(
            "BLOGGER_BLOG_ID is not set. Put it in your .env file "
            "(run `python authorize.py` to see your blog IDs)."
        )
    return blog_id


def _get_service():
    """Build an authenticated Blogger API client using the saved OAuth token."""
    token_file = _path_from_env("GOOGLE_TOKEN_FILE", "credentials/token.json")
    if not token_file.exists():
        raise RuntimeError(
            f"OAuth token not found at {token_file}. "
            "Run `python authorize.py` once to sign in with Google."
        )
    creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)
    if not creds.valid:
        if creds.refresh_token:
            creds.refresh(Request())  # silently gets a new access token
            token_file.write_text(creds.to_json(), encoding="utf-8")
        else:
            raise RuntimeError(
                "Saved token is invalid. Delete credentials/token.json and "
                "run `python authorize.py` again."
            )
    return build("blogger", "v3", credentials=creds, cache_discovery=False)


def _friendly_http_error(err: HttpError) -> str:
    status = getattr(err.resp, "status", "?")
    hint = {
        400: "Bad request - check the title/content/labels you sent.",
        401: "Not authorized - re-run `python authorize.py`.",
        403: "Forbidden - is the Blogger API enabled, and does this Google "
             "account own the blog? Also check quota limits.",
        404: "Blog not found - double-check BLOGGER_BLOG_ID.",
    }.get(status, "Blogger API error.")
    return f"HTTP {status}: {hint} Details: {err}"


# --------------------------------------------------------------------------
# PRIMITIVE 1 of 3 - TOOL (an action with an external side effect)
# --------------------------------------------------------------------------
@mcp.tool()
def publish_blog_post(
    title: str,
    content: str,
    labels: list[str] | None = None,
    content_format: str = "markdown",
    is_draft: bool = False,
) -> dict:
    """Publish a finished blog post to the user's Blogger blog.

    Call this ONLY when the user has approved the final article and asks to
    publish it. It creates a real post through the official Blogger API.

    Args:
        title: The post title.
        content: The full article body, as Markdown (default) or HTML.
        labels: Optional list of Blogger labels/tags, e.g. ["python", "mcp"].
        content_format: "markdown" (converted to HTML for you) or "html".
        is_draft: If True, save as a draft instead of publishing live.

    Returns:
        A dict with `success` (bool). On success it also has `url`,
        `post_id`, `status` and `published`; on failure it has `error`.
    """
    if not title.strip() or not content.strip():
        return {"success": False, "error": "Both title and content are required."}
    if content_format not in ("markdown", "html"):
        return {"success": False, "error": 'content_format must be "markdown" or "html".'}

    body_text = content.strip()
    if content_format == "markdown":
        # Blogger shows the title separately, so drop a duplicate "# Title" line.
        first, _, rest = body_text.partition("\n")
        if first.startswith("# "):
            body_text = rest.strip()
        body_text = md.markdown(body_text, extensions=["extra", "sane_lists"])

    body = {"kind": "blogger#post", "title": title.strip(), "content": body_text}
    if labels:
        body["labels"] = [l.strip() for l in labels if l.strip()]

    try:
        service = _get_service()
        post = (
            service.posts()
            .insert(blogId=_get_blog_id(), body=body, isDraft=is_draft)
            .execute()
        )
    except HttpError as err:
        return {"success": False, "error": _friendly_http_error(err)}
    except Exception as err:  # missing token, missing blog id, network, etc.
        return {"success": False, "error": str(err)}

    return {
        "success": True,
        "status": "draft" if is_draft else "published",
        "post_id": post.get("id"),
        "title": post.get("title"),
        "url": post.get("url"),
        "published": post.get("published"),
    }


# --------------------------------------------------------------------------
# PRIMITIVE 2 of 3 - RESOURCE (read-only data at a URI, no side effects)
# --------------------------------------------------------------------------
@mcp.resource("blogger://posts/recent", mime_type="text/markdown")
def recent_posts() -> str:
    """Recent posts from the user's Blogger blog (read-only context).

    Lists each post's title, URL, publication date and labels so Claude can
    match your existing tone, avoid duplicate topics and suggest internal
    links. This only READS data - it never creates, edits or deletes posts.
    """
    try:
        count = int(os.getenv("BLOGGER_RECENT_POSTS_COUNT", "10"))
    except ValueError:
        count = 10

    try:
        service = _get_service()
        response = (
            service.posts()
            .list(
                blogId=_get_blog_id(),
                maxResults=count,
                orderBy="PUBLISHED",
                fetchBodies=False,
                status=["LIVE"],
            )
            .execute()
        )
    except HttpError as err:
        raise RuntimeError(_friendly_http_error(err)) from err

    items = response.get("items", [])
    if not items:
        return "# Recent Blogger posts\n\n_No published posts found yet._"

    lines = [f"# Recent Blogger posts ({len(items)})", ""]
    for i, post in enumerate(items, start=1):
        labels = ", ".join(post.get("labels", [])) or "none"
        lines += [
            f"{i}. **{post.get('title', '(untitled)')}**",
            f"   - URL: {post.get('url', 'n/a')}",
            f"   - Published: {post.get('published', 'n/a')}",
            f"   - Labels: {labels}",
        ]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# PRIMITIVE 3 of 3 - PROMPT (reusable template the user picks on purpose)
# --------------------------------------------------------------------------
@mcp.prompt()
def create_blog_post(
    topic: str,
    target_audience: str = "general readers",
    style: str = "friendly, clear and practical",
) -> str:
    """Instruction template for writing a well-structured Blogger article.

    The user selects this prompt on purpose and fills in the topic, audience
    and style. It only tells Claude HOW to write the article - it does not
    publish anything.
    """
    return f"""You are an experienced blog writer. Write a complete blog post for my Blogger site.

Topic: {topic}
Target audience: {target_audience}
Writing style: {style}

Before writing, if it helps, read the resource `blogger://posts/recent` so the new
post matches my existing tone and does not repeat a topic I already covered.

Structure the post in Markdown like this:
1. **Title** - a specific, engaging title (as a single `#` heading).
2. **Introduction** - 2-3 short paragraphs: hook the reader, say what the post
   covers and why it matters to {target_audience}.
3. **Body** - 3 to 5 sections, each with a clear `##` heading, useful
   explanations, and a concrete example, code snippet, or step-by-step list
   wherever it makes the idea easier to understand.
4. **Conclusion** - summarize the key takeaways and end with a clear next step
   or call to action.

Also suggest 3-5 short Blogger labels (tags) for the post.

Rules:
- Use simple, accurate language suited to {target_audience}.
- Keep paragraphs short and skimmable.
- Do NOT publish anything yet. Show me the full draft and the suggested labels,
  and wait for my approval. Only when I say to publish, call the
  `publish_blog_post` tool with the approved title, content and labels."""


if __name__ == "__main__":
    # Runs over stdio, which is what Claude Desktop expects.
    try:
        mcp.run(show_banner=False)
    except TypeError:  # older FastMCP versions without show_banner
        mcp.run()