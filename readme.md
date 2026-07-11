# 🤖 MARK XXXIX-OR (39)
### The Ultimate Cross-Platform Personal AI Assistant — By Hebge_Hog

> 📺 **[Watch the full setup video on Tick Tock] (Hebge_Hog) account

A real-time voice AI that can hear, see, understand, and control your computer — on any OS. Supporting Windows, macOS, and Linux. Local execution. Zero subscriptions. Engineered for total autonomy.

---

## ✨ Overview

MARK XXXIX-OR represents the pinnacle of the verity series, evolving into a more flexible and robust system. It bridges the gap between the operating system and human intent. Through natural dialogue, Mark 39 analyzes your screen, processes uploaded documents, and executes complex workflows with a brand-new, adaptive interface.

It's not just an assistant — it's an extension of your digital life.

---

## 🚀 Capabilities

### Core Features
| Feature | Description |
|---|---|
| 🎙️ Real-time Voice | Ultra-low latency conversation in any language |
| 🖥️ System Control | Launch apps, manage files, execute terminal commands |
| 🧩 Autonomous Tasks | High-level planning for complex, multi-step goals |
| 👁️ Visual Awareness | Real-time screen processing and webcam vision |
| 🧠 Persistent Memory | Deeply remembers your projects, preferences, and personal context |
| ⌨️ Hybrid Input | Seamlessly switch between keyboard typing and voice commands |

---

## 🆕 What's New in XXXIX-OR

- 📂 **Advanced File Handling** — New support for direct file uploads. Drop PDFs, source code, or images into the assistant to have them analyzed, summarized, or edited instantly.
- 🎨 **Adaptive & Flexible UI** — A complete overhaul of the interface. The new UI is fully resizable and responsive, featuring transparency controls and customizable layouts to fit your workspace perfectly.
- 🐧🍎 **Refined Cross-Platform Stability** — Major fixes for macOS and Linux compatibility. Core system actions are now more consistent across all three major operating systems.
- ⚡ **Optimized Core Engine** — Significant performance boost in tool-calling logic and response generation, resulting in a 40% faster interaction speed.
- 🔀 **OpenRouter Integration** — Selected action modules (web search, memory, flight finder, desktop control, and more) now route their LLM calls through OpenRouter's free-tier models. This significantly increases the effective request limit without any additional cost, while Gemini Live continues to handle real-time voice and tool-calling.

---

## ⚡ Quick Start

```bash
git clone https://github.com/hackrx321/verity-ai/tree/main.git
cd Mark-XXXIX-OR
pip install -r requirements.txt
playwright install
python main.py
```

> ⚠️ **Installation Note:** To keep the repository lightweight, some OS-specific dependencies are not bundled in `requirements.txt`. If you run into a `ModuleNotFoundError`, simply install the missing package via `pip install <module_name>` for your specific system.

---

## 🟡 This build: Verity edition

This copy has been re-skinned as **Verity** (the smiling AI companion from the
Minecraft "Verity" horror mod) and its voice now comes from **Fish Audio**
instead of Gemini's built-in speech:

- **Get a Fish Audio API key**: https://fish.audio/app/api-keys
- **Free voice, no card needed**: Verity defaults to Fish Audio's `s2.1-pro-free`
  model — their flagship S2.1 Pro model, free under Fair Use through
  **July 24, 2026** (Fish Audio's announcement:
  https://fish.audio/blog/s2-1-pro-free-api/). Same voice cloning, same
  `reference_id`, just no billing required. After that date (or if you hit
  Fair Use limits), add `"fish_model": "s2.1-pro"` to
  `config/api_keys.json` to switch to the paid version.
- **Pick a voice**: browse https://fish.audio/discovery, open a voice you
  like, and copy its **reference ID**. Leave it blank to use Fish Audio's
  default voice.
- On first launch, paste the key (and voice ID, optional) into the setup
  screen. You can also add/edit them any time in `config/api_keys.json`:
  ```json
  {
    "fish_api_key": "your-fish-audio-key",
    "fish_voice_id": "optional-reference-id"
  }
  ```
- Install the new dependency: `pip install fish-audio-sdk` (already in
  `requirements.txt`).
- Every current Gemini Live model is native-audio-only (Google shut down the
  older text-capable Live models in Dec 2025), so Gemini still generates its
  own speech internally — Verity just never plays it. Instead, Gemini's
  output *transcript* gets sent to Fish Audio, which is what you actually
  hear. If Google's model lineup shifts again and `LIVE_MODEL` in `main.py`
  stops working, run:
  ```bash
  python list_live_models.py
  ```
  to see which model your key currently supports, and update `LIVE_MODEL`
  accordingly.

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11 or 3.12 |
| **Microphone** | Required for voice interaction |
| **API Keys** | Free Gemini API key + Free OpenRouter API key |

---

## ⚠️ License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## 👤 Connect with the Creator

Engineered by a developer building a real-world verity-style assistant.
⭐ **Star the repository to support the journey to Mark 100.**

| Platform | Link |
|---|---|
| Tick Tock @Hebge_Hog
