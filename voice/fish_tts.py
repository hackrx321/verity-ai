"""
Fish Audio text-to-speech backend for Verity.

Replaces Gemini's built-in native-audio voice output. Gemini Live now runs in
TEXT-only response mode (see main.py), and every finished reply gets rendered
to speech here via the Fish Audio API, then played back through the same
speaker device the rest of the app already uses (sounddevice).

Setup:
    pip install fish-audio-sdk
    Add to config/api_keys.json:
        "fish_api_key":  "<your Fish Audio API key>"
        "fish_voice_id": "<reference_id of the voice you want, optional>"

    Get an API key at https://fish.audio/app/api-keys
    Browse / clone voices at https://fish.audio/discovery to get a reference_id.
    If fish_voice_id is left blank, Fish Audio's default voice is used.
"""

from __future__ import annotations

import sys
import threading
from pathlib import Path

try:
    from fish_audio_sdk import Session, TTSRequest
except ImportError:  # pragma: no cover
    Session = None
    TTSRequest = None


def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


BASE_DIR    = _base_dir()
CONFIG_FILE = BASE_DIR / "config" / "api_keys.json"

# PCM output settings — must match the sample rate used for playback in main.py
SAMPLE_RATE = 24000
CHANNELS    = 1


class VoiceNotConfigured(Exception):
    """Raised when Fish Audio hasn't been set up yet (no API key)."""


_session_lock = threading.Lock()
_session = None
_session_key = None


def _load_config() -> dict:
    import json
    if not CONFIG_FILE.exists():
        return {}
    try:
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _get_session():
    global _session, _session_key

    if Session is None:
        raise VoiceNotConfigured(
            "fish-audio-sdk isn't installed. Run: pip install fish-audio-sdk"
        )

    cfg = _load_config()
    api_key = cfg.get("fish_api_key", "").strip()
    if not api_key:
        raise VoiceNotConfigured(
            "No 'fish_api_key' found in config/api_keys.json. "
            "Get one at https://fish.audio/app/api-keys"
        )

    with _session_lock:
        if _session is None or _session_key != api_key:
            _session = Session(api_key)
            _session_key = api_key
        return _session


def get_voice_id() -> str | None:
    cfg = _load_config()
    voice_id = cfg.get("fish_voice_id", "").strip()
    return voice_id or None


def get_model() -> str:
    """
    Which Fish Audio backend model to bill against. Defaults to the free
    S2.1 Pro tier (same quality as the paid model, free under Fair Use
    through July 24, 2026 per Fish Audio's announcement). Override in
    config/api_keys.json with "fish_model": "s2.1-pro" once that free
    window closes, or if Fair Use limits become an issue.
    """
    cfg = _load_config()
    return cfg.get("fish_model", "").strip() or "s2.1-pro-free"


def synthesize_pcm(text: str) -> bytes:
    """
    Turn `text` into 16-bit mono PCM audio at SAMPLE_RATE using Fish Audio.
    Raises VoiceNotConfigured if the API key is missing, or the underlying
    fish_audio_sdk exceptions (AuthenticationError, RateLimitError, etc.)
    on API failures.
    """
    text = (text or "").strip()
    if not text:
        return b""

    session = _get_session()
    request = TTSRequest(
        text=text,
        reference_id=get_voice_id(),
        format="pcm",
        sample_rate=SAMPLE_RATE,
        latency="balanced",
    )

    chunks = bytearray()
    for chunk in session.tts(request, get_model()):
        chunks.extend(chunk)
    return bytes(chunks)
