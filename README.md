# 🤖 TARA – Memo-Local Voice Assistant

TARA is a fully offline, privacy-first voice assistant that listens, thinks, speaks, and remembers — without relying on cloud services. It captures your voice input, transcribes it locally using Whisper.cpp, processes it using a locally hosted LLaMA3 language model via Ollama, and speaks the response using Piper TTS.

---

## 📌 Features

- 🎙️ **Voice-to-Text (STT)** via Whisper.cpp (local)
- 🤖 **Local LLM Inference** using LLaMA3:8B with Ollama API
- 🧠 **Memory-Persistent Conversations** (stored in `memory.json`)
- 🔊 **Text-to-Speech (TTS)** using Piper (Docker-based with Wyoming protocol)
- 🌐 **Flask API** for web or programmatic interaction
- 🔐 100% **Offline Execution** (no external API calls)
- 🧹 **Voice-triggered memory clearing**: say _“clear memory”_

---

## 🛠️ Technologies Used

| Component            |        Tool / Framework             |
|----------------------|-------------------------------------|
| **Audio Recording**  | `sounddevice`, `wave` (Python)      |
| **Transcription**    | `whisper.cpp` + `ggml-base.en.bin`  |
| **LLM Inference**    | `LLaMA3` via `Ollama` (localhost API)|
| **Backend**          | `Flask`, `asyncio`, `json`          |
| **TTS**              | `Piper` (Docker) + Wyoming Protocol |
| **Memory Storage**   | Local `memory.json` file            |
| **API Testing**      | Postman, Browser                    |

---

## 🧩 Architecture Overview

![archtara1](https://github.com/user-attachments/assets/27b45a43-6838-40f1-9dd0-1ecdc252e5cf)

## WorkFlow

1. 🎧 **`record_audio.py`** captures user audio as `output.wav`
2. 🧠 **`whisper.cpp`** transcribes the audio → `output.txt`
3. 🧩 **`assistant.py`** processes the text:
   - If "clear memory" → clears `memory.json`
   - Else → sends context + prompt to LLaMA3 via Ollama
4. 🧠 Response is saved in memory (`memory.json`)
5. 🔊 Reply is spoken via Piper TTS and played back
6. 🌐 Optional: Interact via REST API

---

## 🌐 Flask API Endpoints

| Method | Route         | Description                                   |
|--------|---------------|---------------------------------------------- |
| POST   | `/transcribe` | Runs full pipeline (record → respond → speak) |
| POST   | `/ask`        | Accepts direct text input, responds & speaks  |
| GET    | `/memory`     | Returns recent conversation history           |

---

## 📦 Setup Instructions

### ✅ Prerequisites
- Python 3.9+
- Docker installed
- `whisper.cpp` built from source
- LLaMA3 model running via Ollama
- Piper TTS model (e.g., `en_US-lessac-medium`) downloaded

### 🔧 Setup Steps

**1. Clone the repo**
```bash
git clone https://github.com/your-username/tara-voice-assistant
cd tara-voice-assistant
```

**2. Install dependencies**
```
pip install -r requirements.txt
```

**3. Build whisper.cpp (Windows / CMake)**
```
Follow: https://github.com/ggerganov/whisper.cpp
```

**4. Download Whisper and Piper models**
```
Whisper: ggml-base.en.bin
Piper: en_US-lessac-medium.onnx + .onnx.json
```

**5. Run Piper TTS in Docker**
```
docker run -it --rm -v "$HOME/piper/voices:/voices" -p 10200:10200 rhasspy/piper --voice en/en_US-lessac-medium
```

**6. Start Ollama (LLaMA3 model)**
```
ollama run llama3:8b
```

**7. Start the Flask server**
```
python app.py
```
---
## 🧪 Testing the Assistant

You can test it using:

- 🎤 **Voice interaction** via [`POST /transcribe`]
- 💬 **Text prompt** via [`POST /ask`]
- 🧠 **Memory inspection** via [`GET /memory`]

You can use **Postman**, **browser**, or any HTTP client to call the endpoints.

---

## 📁 Project Structure

```bash
.
├── app.py                # Flask backend
├── assistant.py          # Core pipeline logic
├── record_audio.py       # Voice recorder
├── my_tts.py             # Piper TTS connection
├── llm.py                # LLaMA3 response handler
├── memory.json           # Stores assistant memory
├── output.txt / .wav     # Temp transcription/output
└── Docker & Model Setup  # External setup
```
---

## Use Cases

🔐 Secure offline voice assistant — no cloud dependency

🧠 Privacy-focused AI environments — sensitive data never leaves device

🗣️ Voice-controlled automation — trigger local commands or responses

🏠 Smart home or embedded voice apps — lightweight and efficient

💬 Voice journaling or mental health companion — with memory retention

🌐 Offline assistant in remote areas — works without internet

---

## 🙋‍♂️ Author

• Mentor / Manager: Mr. Venkata Ramana Sudhakar Polavarapu

• Mudimala Yeshwanth Goud

 🛠️ Passionate about AI/ML, NLP, RAG, Data Science, system programming, full-stack development, and intelligent assistant systems.


---
## 📬 Contact
For questions or collaboration, you can reach out at:

**Email 📧** : yeshwanth.mudimala@motivitylabs.com
