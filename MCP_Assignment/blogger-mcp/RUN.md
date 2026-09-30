# How to run - command cheat sheet (Windows)

Open **Command Prompt** in the extracted `blogger-mcp` folder. Requires Python 3.10+.

## 1. Install (once)

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Shortcut: run `setup.bat` instead of the four lines above.

## 2. Google setup (once, in the browser)

1. <https://console.cloud.google.com/> -> create a project.
2. **APIs & Services -> Library** -> enable **Blogger API v3**.
3. **OAuth consent screen** -> External -> add **your Google account as a Test user**.
4. **Credentials -> Create credentials -> OAuth client ID -> Desktop app** -> Download JSON.
5. Rename it to `client_secret.json` and put it in the `credentials\` folder.

## 3. Sign in and get your Blog ID (once)

```bat
python authorize.py
```

Approve access in the browser. The script prints your blog IDs. Put yours in `.env`:

```
BLOGGER_BLOG_ID=1234567890123456789
```

## 4. Test that everything works

```bat
python test_server.py
```

You should see `[PASS]` for: exactly 1 tool, 1 resource, 1 prompt, and the prompt rendering. The resource line passes once steps 2-3 are done.

## 5. Run the server

```bat
python server.py
```

(It waits silently for a client - that's normal. `Ctrl+C` to stop.)

## 6. Connect to Claude Desktop

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "blogger": {
      "command": "C:\\Users\\YOURNAME\\blogger-mcp\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\YOURNAME\\blogger-mcp\\server.py"],
      "env": { "PYTHONIOENCODING": "utf-8" }
    }
  }
}
```

Fully quit and reopen Claude Desktop.

## 7. Try it in Claude Desktop

1. **Prompt:** `+` -> `blogger` -> `create_blog_post` -> enter a topic.
2. **Resource:** `+` -> Add from blogger -> `blogger://posts/recent`.
3. **Tool:** say *"Save this as a draft on Blogger with labels x, y"*, then *"Publish it live."*

## Quick fixes

- Token expired (`invalid_grant`): `del credentials\token.json` then `python authorize.py`.
- Access blocked in browser: add yourself as a **Test user** on the OAuth consent screen.
- Wrong blog / 404: fix `BLOGGER_BLOG_ID` in `.env`.
- Logs: `%APPDATA%\Claude\logs\mcp-server-blogger.log`.

More detail: see `README.md`.
