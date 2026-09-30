# Blogger Publishing Assistant MCP

## Use case

I write blog posts for my Blogger site and want Claude to help me from idea to live post: draft the article in my style, then publish it without me copy-pasting into the Blogger editor. This FastMCP server connects Claude to the official Google Blogger API so the whole flow happens inside one conversation.

```
User  ->  Claude  ->  Blogger MCP (server.py)  ->  Blogger API  ->  My Blogger blog
```

The server has **exactly 3 primitives**: one tool, one resource, one prompt.

| Primitive | Name | Type |
|-----------|------|------|
| Tool      | `publish_blog_post`     | action |
| Resource  | `blogger://posts/recent` | read-only data |
| Prompt    | `create_blog_post`      | instruction template |

## Why each primitive was chosen

### Tool: `publish_blog_post`
Publishing a blog post is an **action that creates an external side effect** (a new public post appears on my blog). It takes input (title, content, labels), does something, and returns a result (success + URL). It is also something the model should decide to call **mid-conversation**, once I approve the draft. That is exactly what a tool is for.

### Resource: `blogger://posts/recent`
My recent Blogger posts are **addressable data** that Claude can pull into context ("here's the data at this URI"). Reading them changes nothing, so there are no side effects and it is not an action. Having it as a resource lets Claude match my tone and avoid repeating topics.

### Prompt: `create_blog_post`
Blog-writing instructions are a **reusable template that I select on purpose** and fill in (topic, audience, style). It does not do anything itself; it only tells Claude how to write a well-structured article. That makes it a prompt, not a tool or a resource.

## How the three work together

1. **Prompt** - I pick `create_blog_post` and give a topic. Claude gets a structured set of writing instructions.
2. **Resource** - Claude reads `blogger://posts/recent` to see my existing posts (tone, topics, labels).
3. **Tool** - Claude shows me the draft. When I say "publish it", Claude calls `publish_blog_post` and gives me the live URL.

## Project structure

```
blogger-mcp/
|-- server.py            # FastMCP server: the 1 tool + 1 resource + 1 prompt
|-- authorize.py         # one-time Google OAuth sign-in helper (not an MCP primitive)
|-- test_server.py       # proves 1 tool / 1 resource / 1 prompt
|-- requirements.txt     # Python dependencies
|-- setup.bat            # one-step Windows setup (venv + install)
|-- .env.example         # copy to .env and fill in BLOGGER_BLOG_ID
|-- .gitignore           # keeps secrets out of git
|-- credentials/
|   |-- README.txt
|   |-- client_secret.json   # YOU add this (from Google Cloud)
|   `-- token.json           # created by authorize.py
|-- README.md
`-- RUN.md               # quick command cheat-sheet
```

## Installation (Windows)

Requires **Python 3.10+** (install from python.org and tick "Add Python to PATH").

Open **Command Prompt** or **PowerShell** in the project folder:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

(Or just double-click / run `setup.bat`, which does the same.)

## Google Cloud / Blogger API setup

1. Go to <https://console.cloud.google.com/> and **create a project** (e.g. "Blogger MCP").
2. Open **APIs & Services -> Library**, search for **Blogger API v3**, click **Enable**.

## OAuth 2.0 setup

1. **APIs & Services -> OAuth consent screen** (may be called *Google Auth Platform*):
   - User type: **External**, fill in an app name and your email.
   - Under **Test users**, **add your own Google account** (the one that owns the blog).
2. **APIs & Services -> Credentials -> Create credentials -> OAuth client ID**:
   - Application type: **Desktop app**.
   - Click **Download JSON**.
3. Rename the file to `client_secret.json` and put it in the `credentials/` folder.
4. Run the one-time sign-in:

   ```bat
   python authorize.py
   ```

   A browser opens -> choose your Google account -> click **Continue** (Google warns the app is unverified because it is your own test app; that is normal) -> allow Blogger access.
5. The script saves `credentials/token.json` and **prints your blog IDs**. Copy the right one.
6. Open `.env` and set it:

   ```
   BLOGGER_BLOG_ID=1234567890123456789
   ```

> Nothing secret is in the code. `client_secret.json`, `token.json` and `.env` are local files and are listed in `.gitignore`.

## Run the server

```bat
venv\Scripts\activate
python server.py
```

It will sit silently waiting for a client (that is normal - it speaks MCP over stdio). Press `Ctrl+C` to stop. Normally you do not run it by hand; Claude Desktop starts it for you.

## Connect to Claude Desktop

1. Open `%APPDATA%\Claude\claude_desktop_config.json` (in Claude Desktop: **Settings -> Developer -> Edit Config**).
2. Add this (change `YOURNAME` and the folder to your real path; use double backslashes):

```json
{
  "mcpServers": {
    "blogger": {
      "command": "C:\\Users\\YOURNAME\\blogger-mcp\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\YOURNAME\\blogger-mcp\\server.py"],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

If the file already has other servers, just add `"blogger": {...}` inside the existing `mcpServers`.

3. **Fully quit Claude Desktop** (right-click the tray icon -> Quit) and reopen it.
4. You should see the `blogger` server in the tools/connectors menu.

The server reads `BLOGGER_BLOG_ID` from your `.env` file, so it does not need to be in this config.

## Test procedure

### A. Structure test (no Google login needed for most of it)

```bat
python test_server.py
```

Expected:

```
[PASS] exactly 1 tool: ['publish_blog_post']
[PASS] exactly 1 resource: ['blogger://posts/recent']
[PASS] no extra resource templates
[PASS] exactly 1 prompt: ['create_blog_post']
[PASS] prompt renders with the topic and required structure
[PASS] resource returned data:   <- after you finish OAuth setup; otherwise [SKIP]
```

If you have not signed in yet, the resource line shows `[SKIP]` and an error traceback may print - that is expected until `authorize.py` is done.

### B. Test in Claude Desktop

1. **Prompt** - click the **+** in the chat box -> choose the `blogger` server -> pick **create_blog_post**, fill in a topic (e.g. "Why every beginner should learn Git"). Claude writes a structured draft and does *not* publish.
2. **Resource** - click **+ -> Add from blogger -> blogger://posts/recent**. Claude now has your recent posts in context. Ask: *"Which of my recent posts is most related to this draft?"*
3. **Tool** - say: *"Save this as a **draft** on Blogger with labels git, beginners."* Claude calls `publish_blog_post` with `is_draft=true`. Check Blogger -> **Posts -> Drafts**. When happy: *"Publish it live."*

### Example conversations

- "Use the create_blog_post prompt for the topic 'Python virtual environments' for beginners."
- "Look at my recent posts and suggest a topic I haven't covered."
- "Publish this post with the labels python and tutorial."

## Troubleshooting

| Problem | Cause / Fix |
|---|---|
| `OAuth token not found` | Run `python authorize.py` first. |
| `client_secret.json not found` | Download the **Desktop app** OAuth JSON, rename it, put it in `credentials/`. |
| Browser says **"Access blocked / app not verified / 403 access_denied"** | Add your Google account under **OAuth consent screen -> Test users**. |
| `invalid_grant` / `Token has been expired or revoked` | Apps in "Testing" mode expire refresh tokens after **7 days**. Delete `credentials/token.json` and run `python authorize.py` again. |
| `HTTP 403 ... Blogger API has not been used` | Enable **Blogger API v3** in the same Google Cloud project as your OAuth client. |
| `HTTP 403 ... insufficient` / `forbidden` | Sign in with the Google account that **owns** the blog. Delete `token.json` and re-authorize. |
| `HTTP 404 Blog not found` | Wrong `BLOGGER_BLOG_ID`. Re-run `authorize.py` to list your IDs. |
| `BLOGGER_BLOG_ID is not set` | Make sure `.env` exists (copy from `.env.example`) and has the ID. |
| Server not showing in Claude Desktop | Check JSON syntax (commas, double backslashes), use the full path to `venv\Scripts\python.exe`, then **fully quit** and reopen Claude Desktop. Logs: `%APPDATA%\Claude\logs\mcp-server-blogger.log`. |
| `'python' is not recognized` | Reinstall Python and tick **Add Python to PATH**. |
| Weird Unicode errors on Windows | Keep `"PYTHONIOENCODING": "utf-8"` in the Claude Desktop config. |
| Draft has no live URL | Drafts get a preview-style URL until published; publish from Blogger or ask Claude again with `is_draft=false`. |
