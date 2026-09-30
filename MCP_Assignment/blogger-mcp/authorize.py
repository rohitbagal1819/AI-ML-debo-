"""
One-time Google sign-in (OAuth 2.0) for the Blogger MCP.

Run:  python authorize.py

It opens your browser, asks you to allow access to Blogger, then saves a token
to credentials/token.json. It also prints the IDs of your blogs so you can put
the right one in .env as BLOGGER_BLOG_ID.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
SCOPES = ["https://www.googleapis.com/auth/blogger"]


def _p(name: str, default: str) -> Path:
    p = Path(os.getenv(name, default))
    return p if p.is_absolute() else BASE_DIR / p


def main() -> None:
    secrets = _p("GOOGLE_CLIENT_SECRETS_FILE", "credentials/client_secret.json")
    token = _p("GOOGLE_TOKEN_FILE", "credentials/token.json")

    if not secrets.exists():
        sys.exit(
            f"ERROR: {secrets} not found.\n"
            "Download your OAuth 'Desktop app' client JSON from Google Cloud "
            "Console and save it there (see README.md, step 2)."
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(secrets), SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")
    token.parent.mkdir(parents=True, exist_ok=True)
    token.write_text(creds.to_json(), encoding="utf-8")
    print(f"\nSaved token to {token}")

    service = build("blogger", "v3", credentials=creds, cache_discovery=False)
    blogs = service.blogs().listByUser(userId="self").execute().get("items", [])
    if not blogs:
        print("No blogs found on this Google account.")
        return
    print("\nYour blogs (copy the ID you want into .env as BLOGGER_BLOG_ID):")
    for b in blogs:
        print(f"  {b['id']}   {b['name']}   {b['url']}")


if __name__ == "__main__":
    main()
