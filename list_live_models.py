"""
Run this once to find out which Gemini model your API key can actually use
for the Live API (the bidirectional voice/text session Verity uses).

Usage:
    python list_live_models.py
    python list_live_models.py YOUR_GEMINI_API_KEY

If you haven't run main.py's setup screen yet, config/api_keys.json won't
exist — either pass your key as an argument, or just paste it in when asked.

It prints every model your key can see, and flags the ones that support
"bidiGenerateContent" (Live API). Copy one of the flagged names into
LIVE_MODEL near the top of main.py.
"""
import json
import sys
from pathlib import Path

from google import genai

BASE_DIR = Path(__file__).resolve().parent
API_FILE = BASE_DIR / "config" / "api_keys.json"


def get_api_key() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1].strip()

    if API_FILE.exists():
        try:
            keys = json.loads(API_FILE.read_text(encoding="utf-8"))
            key = keys.get("gemini_api_key", "").strip()
            if key:
                return key
        except Exception:
            pass

    return input("Paste your Gemini API key: ").strip()


def main():
    api_key = get_api_key()
    if not api_key:
        print("No API key given — aborting.")
        return

    client = genai.Client(api_key=api_key)

    print("\nModels that support the Live API (bidiGenerateContent) on this key:\n")
    found = False
    for m in client.models.list():
        actions = getattr(m, "supported_actions", None) or []
        if "bidiGenerateContent" in actions:
            found = True
            print(f"  {m.name}")

    if not found:
        print("  (none found — printing every model instead, check manually)\n")
        for m in client.models.list():
            actions = getattr(m, "supported_actions", None) or []
            print(f"  {m.name:55s} {actions}")

    print("\nCopy one of the bidiGenerateContent-capable names above into "
          "LIVE_MODEL in main.py (keep the 'models/' prefix if it's shown).")


if __name__ == "__main__":
    main()
