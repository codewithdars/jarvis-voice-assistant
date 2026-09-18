# 🤖 JARVIS – AI Voice Assistant

JARVIS is a Python-based AI voice assistant designed to interact with users through voice commands. It can recognize speech, open websites, play music, and use Gemini AI to answer questions and handle commands.

## 🚀 Features

- 🎙️ Voice command recognition
- 🧠 Gemini AI integration
- 🌐 Open websites using voice commands
- 🎵 Search and play songs
- 🔎 Intelligent command processing
- 🔊 Text-to-speech responses
- 💬 Natural voice interaction
- 🛑 Voice-controlled exit
- ⚡ Fast and lightweight Python implementation

## 🛠️ Tech Stack

- Python
- Google Gemini API
- SpeechRecognition
- PyAudio
- pyttsx3
- yt-dlp
- Web Browser
- VS Code

## 📂 Project Structure

```text
_voice-assistant/
│
├── main.py
├── musicLibrary.py
├── README.md
├── .gitignore
│
└── .venv/

⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd _voice-assistant
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment
For Windows PowerShell:
.\.venv\Scripts\Activate.ps1
4. Install Dependencies
python -m pip install google-genai SpeechRecognition pyttsx3 yt-dlp
For microphone support:
python -m pip install "SpeechRecognition[audio]"
🔑 Gemini API Key
JARVIS uses the Gemini API for AI-powered responses.
Set your Gemini API key as an environment variable:
GEMINI_API_KEY=YOUR_API_KEY

▶️ Run JARVIS
After activating the virtual environment, run:
python main.py
JARVIS will start listening for the wake word:
Jarvis
Then speak your command.
🎤 Example Commands
Jarvis
→ Open Google

Jarvis
→ Open YouTube

Jarvis
→ Open Instagram

Jarvis
→ Open LinkedIn

Jarvis
→ Play Believer

Jarvis
→ What is Artificial Intelligence?

Jarvis
→ Explain Machine Learning
🧠 How It Works
Voice Input
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Direct Commands  Gemini AI
 │               │
 ▼               ▼
Web / Music      AI Response
 │               │
 └───────┬───────┘
         ▼
   Text-to-Speech
         ↓
       JARVIS
🔮 Future Improvements
- 🖥️ Computer control
- 📁 File and folder management
- 🌦️ Weather information
- 📰 News updates
- 🧠 Long-term memory
- ⏰ Reminders and alarms
- 📧 Email automation
- 🔐 Secure authentication
- 🗣️ Continuous conversation mode
- 🎵 Direct audio playback
- 🧩 Modular plugin system
📌 Project Status
🚧 Currently in Development
JARVIS is an ongoing project and new features are being added regularly.
👨‍💻 Author
Aadarsh
B.Tech CSE-AI
Interests
- Artificial Intelligence
- Machine Learning
- Python
- Web Development
- Automation
⭐ If you find this project interesting, consider giving it a star!
