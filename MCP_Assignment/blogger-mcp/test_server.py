"""
Test script: proves the server has EXACTLY 1 tool, 1 resource and 1 prompt,
and that the prompt (and, if you are signed in, the resource) work.

Run:  python test_server.py
"""

import asyncio
import sys

from fastmcp import Client

from server import mcp


def check(ok: bool, message: str) -> None:
    print(("[PASS] " if ok else "[FAIL] ") + message)
    if not ok:
        sys.exit(1)


async def main() -> None:
    async with Client(mcp) as client:
        tools = await client.list_tools()
        resources = await client.list_resources()
        templates = await client.list_resource_templates()
        prompts = await client.list_prompts()

        check(len(tools) == 1 and tools[0].name == "publish_blog_post",
              f"exactly 1 tool: {[t.name for t in tools]}")
        check(len(resources) == 1 and str(resources[0].uri) == "blogger://posts/recent",
              f"exactly 1 resource: {[str(r.uri) for r in resources]}")
        check(len(templates) == 0, "no extra resource templates")
        check(len(prompts) == 1 and prompts[0].name == "create_blog_post",
              f"exactly 1 prompt: {[p.name for p in prompts]}")

        result = await client.get_prompt(
            "create_blog_post",
            {"topic": "Getting started with MCP", "target_audience": "beginners"},
        )
        text = result.messages[0].content.text
        check("Getting started with MCP" in text and "Conclusion" in text,
              "prompt renders with the topic and required structure")

        # The resource needs Google sign-in, so it is only tested if configured.
        try:
            data = await client.read_resource("blogger://posts/recent")
            print("[PASS] resource returned data:\n")
            print(data[0].text)
        except Exception as err:
            print(f"[SKIP] resource not read (finish setup first): {err}")

    print("\nAll structure checks passed.")


if __name__ == "__main__":
    asyncio.run(main())
