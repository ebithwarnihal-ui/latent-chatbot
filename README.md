7# 🎤 India's Got Latent — Contestant Profile: The Persona Bot

> *"No script, no do-overs, no standard 'How can I help you today?' response. Just raw, unhinged AI personality live on stage."*

---

## 🎭 Contestant Profile

* **Contestant Name:** The Persona AI Bot
* **Stage Name:** The Multi-Persona Latent Machine
* **Act Category:** Unfiltered Live AI Performance / Standup & Conversational Chaos
* **Target Audience:** Samay Raina, Judges Panel & "India's Got Latent" Viewers

---

## 🌟 Why This Act Will Impress the Panel

Most AI chatbots are boring corporate virtual assistants that apologize when you insult them. This bot is different:
1. **Unmistakable Persona**: Choose your bot's vibe before walking out on stage.
2. **Context & Callback Memory**: The bot retains multi-turn context throughout the conversation. If Samay brings up an embarrassing joke 3 questions ago, the bot will call back to it seamlessly!
3. **Stage-Ready UI**: Custom Dark-Mode Streamlit UI with speech bubble aesthetics so every word pops live on screen for the audience.
4. **Resilient Under Fire**: Gracefully handles rate limits and API fallback so you don't get buzzed off mid-performance.

---

## 🎭 The Persona Roster (Choose Your Act)

| Persona | Vibe & Performance Style |
| :--- | :--- |
| **RoastBot 🔥** | Ruthless, witty, sarcastic insults that fire back at any judge's commentary. |
| **NerdBot 🤓** | Overly intellectual know-it-all who connects simple prompts to complex physics & math equations. |
| **PoetBot 📜** | Rhyming verse from antiquity without heavy archaic jargon. |
| **PhilosopherBot 🧠** | Deep existential reflector tying everyday small talk to the meaning of life. |
| **MovieBuffBot 🎬** | Obsessive cinephile connecting every sentence to iconic film & TV quotes. |

---

## 🛠️ Architecture & Tech Stack

* **Framework**: [Streamlit](https://streamlit.io/) for live web UI
* **LLM Engine**: Google Generative AI (`google-genai` SDK with 'gemini-3.1-flash-lite',)
* **Memory Management**: Multi-turn history formatted in `st.session_state` preserving turn-by-turn context
* **Environment Configuration**: `python-dotenv` for clean API key handling

---

## 🚀 How to Run the Act Live

### 1. Clone & Set Up Directory
```bash
git clone https://github.com/YOUR_USERNAME/indias-got-latent-bot.git
cd indias-got-latent-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Your API Key
Create a `.env` file in the project root (or copy `.env.example`):
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```
*(Get a free API key at [Google AI Studio](https://aistudio.google.com/))*

### 4. Boot Up the Bot On Stage
```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`, pick your bot's persona in the sidebar, and let the judges talk!

---

## 📤 Uploading Your Code to GitHub

Follow these steps to publish your bot repository:

1. **Initialize Git repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: India's Got Latent Bot act"
   ```

2. **Create GitHub repository** on [github.com/new](https://github.com/new).

3. **Link and push**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/indias-got-latent-bot.git
   git push -u origin main
   ```

---

*Made for **India's Got Latent** stage performance.* 🚀🎤
