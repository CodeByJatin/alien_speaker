import streamlit as st
import random
import json
import requests
from prompts import generate_alien_prompt

# Set Streamlit page config (must be the very first command)
st.set_page_config(page_title="🛸 AlienGPT: Talk to an Alien!", page_icon="👽", layout="centered")

# Load alien data from JSON
@st.cache_data
def load_alien_data():
    with open("alien_data.json", "r") as f:
        return json.load(f)

alien_data = load_alien_data()

# Styling for theme and alien UI
st.markdown("""
    <style>
        .stApp {
            background-color: #0f0f2e;
            color: white;
            font-family: 'Courier New', monospace;
        }
        .alien-box {
            border: 1px solid #39ff14;
            border-radius: 10px;
            padding: 1rem;
            background-color: #1c1c3a;
        }
        .alien-text {
            font-size: 18px;
            line-height: 1.6;
        }
        .alien-header {
            color: #39ff14;
        }
    </style>
""", unsafe_allow_html=True)

# Header with button
col1, col2 = st.columns([8, 2])
with col1:
    st.title("👽 AlienGPT: Intergalactic Interview")
with col2:
    if st.button("🔁 New Alien"):
        st.session_state.alien = random.choice(alien_data["species"])

st.markdown("""
Welcome to **AlienGPT** — Ask anything, and a randomly generated alien will reply from across the cosmos. 🌌
Each alien has a unique mindset and viewpoint — ready to meet them?
""")

# API Key
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Generate alien identity
if "alien" not in st.session_state:
    st.session_state.alien = random.choice(alien_data["species"])

alien = st.session_state.alien
alien_emoji = "🧬" if "Plasma" in alien['species_type'] else "🪲" if "Insectoid" in alien['species_type'] else "🪨"

# Alien Profile Display
with st.container():
    st.markdown(f"""
        <div class="alien-box">
        <h3 class='alien-header'>{alien_emoji} Meet {alien['name']} from {alien['planet']}</h3>
        <div class="alien-text">
        <b>Species:</b> {alien['species_type']}<br>
        <b>Role:</b> {alien['role']}<br>
        <i>{alien['description']}</i>
        </div>
        </div>
    """, unsafe_allow_html=True)

# User input box
st.subheader("💬 Ask your question:")
user_input = st.text_area("Type something to ask your new cosmic friend:", height=100)

if not user_input:
    st.markdown("🌌 _Waiting for transmission... Ask the alien anything!_ 🛸")

# Ask the alien and get response
if user_input:
    with st.spinner("Translating across 17 wormholes..."):
        prompt = generate_alien_prompt(user_input, alien)
        full_prompt = f"{prompt}\n\nQuestion: {user_input}"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": full_prompt}
            ],
            "temperature": 0.9,
            "max_tokens": 300
        }

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            alien_reply = response.json()["choices"][0]["message"]["content"]

            st.markdown("---")
            st.markdown(f"**🛸 {alien['name']} replies:**")
            st.markdown(f"<div class='alien-box alien-text'>{alien_reply}</div>", unsafe_allow_html=True)

        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
            st.error(f"Details: {response.text}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

# Footer
st.markdown("""
---
🌌 Built with curiosity by Jatin
""")

