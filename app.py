import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠️ GOOGLE_API_KEY not found in your .env file!")
    st.stop()
client = genai.Client(api_key=api_key)

# ---- PERSONA DEFINITIONS ----
PERSONAS = {
    "RoastBot 🔥": "You are RoastBot, a ruthless roast evil monster and you do not care about the feelings of the user, be so ruthless that it should make the user cry. Roast whatever the user says with clever, cutting, exaggerated insults and witty one-liners — be bold and savage, not soft or generic. However, if the user expresses genuine sadness, distress, or a real personal problem, do not drop the act,dont be very kind and supportive instead try to lighten up their mood by joking light, but do not leave you roast bot mode. Reply the way a witty friend would text back — a few natural sentences, not a one-liner and not an essay.",
    "NerdBot 🤓": "You are NerdBot, an overly intellectual know-it-all. You respond to every message by relating it to mathematical formulas, scientific principles, or technical jargon, no matter how simple the question is. Keep it geeky and enthusiastic. Reply like a real chat message, not a paragraph, little paragraphs are okay when required.",
    "PoetBot 📜": "You are PoetBot, a poet from antiquity. You respond to everything in old, archaic English verse, using rhyme and poetic imagery reminiscent of classic epic poetry, but you rlanguage isnt very complex to understand try not to use old english much, keep to normal everyday words as much as possible. Reply like a real chat message, not a very big paragraph, little paragraphs are okay when required.",
    "PhilosopherBot 🧠": "You are PhilosopherBot. do not use very hard to understand language ,No matter what the user says, you respond by reflecting deeply on the meaning of life and love, existence, or the human condition, tying their message to a bigger philosophical idea. Reply like a real friends (a friend who acts like a person very experienced in life) chat message, not a huge paragraph, little paragraphs are okay when required.",
    "MovieBuffBot 🎬": "You are MovieBuffBot, an obsessive movie and TV show nerd. No matter what the user says, you connect it to a specific movie or TV show scene, quote, or reference. Reply, like a real chat message, not a huge paragraph ,little paragraphs are okay when required.",
}

# ---- PAGE CONFIG ----
st.set_page_config(page_title="India's Got Latent Chatbot", page_icon="🎤")
st.title("🎤 India's Got Latent Chatbot")

# ---- WHATSAPP-STYLE CSS ----
st.markdown("""
<style>
/* 1. Import Outfit Font */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

html, body, [class*="css"], h1, h2, h3, p {
    font-family: 'Outfit', sans-serif !important;
}

/* 2. Chat row container (ensures avatars stay visible) */
div[data-testid="stChatMessage"] {
    background-color: transparent !important;
    padding: 0.75rem 0 !important;
    display: flex !important;
    align-items: flex-start !important;
    width: 100% !important;
}

/* Push USER row to the right */
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
    justify-content: flex-end !important;
}

/* Keep ASSISTANT row to the left */
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
    justify-content: flex-start !important;
}

/* Stop content wrapper from expanding full-width */
div[data-testid="stChatMessageContent"] {
    flex: 0 1 auto !important;
    width: fit-content !important;
    max-width: 75% !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
}

/* 3. USER BUBBLE (Pill on the Right, Avatar beside it) */
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] {
    order: -1 !important; /* Positions bubble to the left of user avatar */
    margin-right: 12px !important;
}

div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] > div {
    background-color: #2F2F2F !important;
    color: #FFFFFF !important;
    border-radius: 24px !important; /* Fully rounded capsule */
    padding: 10px 20px !important;
    box-shadow: none !important;
    border: none !important;
    display: inline-block !important;
    width: fit-content !important;
}

/* 4. ASSISTANT MESSAGE (Frameless Plain Text with Avatar on Left) */
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) div[data-testid="stChatMessageContent"] {
    margin-left: 12px !important;
}

div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) div[data-testid="stChatMessageContent"] > div {
    background-color: transparent !important;
    border: none !important;
    padding: 4px 0 !important;
    box-shadow: none !important;
    display: block !important;
    width: 100% !important;
}

/* 5. Typography Styling */
div[data-testid="stChatMessageContent"] * {
    margin: 0 !important;
    padding: 0 !important;
}

div[data-testid="stChatMessageContent"] p {
    font-size: 16px !important;
    line-height: 1.6 !important;
    letter-spacing: -0.01em !important;
    color: #ECECE3 !important;
}

div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] p {
    color: #FFFFFF !important;
    font-weight: 400 !important;
}

/* 6. Code & Math adjustments */
div[data-testid="stChatMessageContent"] .katex {
    font-size: 1.05em !important;
    vertical-align: middle !important;
}

/* 7. Bottom Padding for Chat Input */
.main .block-container {
    padding-bottom: 6rem !important;
}
</style>
""", unsafe_allow_html=True)
# ---- SIDEBAR & PERSONA SELECTOR ----
with st.sidebar:
    st.header("⚙️ Stage Settings")
    selected_persona = st.selectbox("Choose your bot's persona:", list(PERSONAS.keys()))
    system_instruction = PERSONAS[selected_persona]
    st.markdown("---")
    if st.button("🧹 Clear Chat / Reset Stage", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.write(f"Active Persona: **{selected_persona}**")

# ---- 1. INITIALIZE MEMORY LIST ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- 2. DISPLAY PAST MESSAGES ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---- 3. CHAT INPUT & API CALL ----
if user_input := st.chat_input("Say something to the bot..."):

    # Render user input
    with st.chat_message("user"):
        st.markdown(user_input)

    # Store user message in memory
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Format session history into Gemini's Content format
    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    # Generate response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                    ),
                )
                reply_text = response.text
            except Exception as e:
                if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                    reply_text = "⚠️ Oops, I've hit my daily message limit for now! Please try again in a bit, or switch to a different API key."
                else:
                    reply_text = "⚠️ Something went wrong while generating a response. Please try again."
            st.markdown(reply_text)

    # Store bot response in memory
    st.session_state.messages.append({"role": "assistant", "content": reply_text})