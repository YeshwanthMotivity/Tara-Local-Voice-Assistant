# assistant.py
import subprocess
import asyncio
import os
import json

from llm import get_response
from my_tts import speak

WHISPER_PATH = r"C:\Yash\mem0-assistant\Memo_assistant\whisper.cpp\build\bin\Release\whisper-cli.exe"
MODEL_PATH = r"C:\Yash\mem0-assistant\Memo_assistant\models\ggml-base.en.bin"
AUDIO_INPUT = "output.wav"
MEMORY_FILE = "memory.json"

def transcribe_audio():
    print("🗣️ Transcribing using Whisper...")
    result = subprocess.run(
        [WHISPER_PATH, "-m", MODEL_PATH, "-f", AUDIO_INPUT, "-otxt", "-of", "output"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("❌ Whisper failed:", result.stderr)
        return None 

    with open("output.txt", "r") as f:
        return f.read().strip()

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def append_to_memory(user_input, reply, max_memory=50):
    memory = load_memory()
    memory.append({"user": user_input, "assistant": reply})
    memory = memory[-max_memory:]  # Keep only last `max_memory` entries
    save_memory(memory)


async def main():
    print("🎤 Say something! (recording...)")
    os.system("python record_audio.py")

    text = transcribe_audio()
    if not text:
        print("❌ No transcription available.")
        return

    print("🧠 You said:", text)

    if "clear memory" in text.lower():
        save_memory([])  # Clears memory
        reply = "I have cleared all your memory."
    else:
        reply = get_response(text)
        append_to_memory(text, reply)

    print("🤖 Assistant:", reply)
    print("🔊 Speaking...")
    await speak(reply)
    print("✅ Done. Check test_output.wav")


if __name__ == "__main__":
    asyncio.run(main())
