# 🛸 AlienGPT: Intergalactic Interview Simulator

AlienGPT is a fun and interactive AI project that simulates conversations with randomly generated alien beings. Each alien has a unique personality, background, and way of communicating. Great for fun chats, creative storytelling, or exploring unique perspectives.

---

## 🚀 Features

- Random alien character generation from distant planets 🌌  
- Rich profiles including species, role, personality, and background  
- Ask any question and get a unique alien-style response  
- Clean, dark-themed UI styled using Streamlit  
- Powered by LLaMA-3 via GROQ API

---

## ⚙️ Installation & Usage

### ✅ Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/aliengpt.git
cd aliengpt
```

### ✅ Step 2: Install Requirements

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Set Up GROQ API Key

Create a `.streamlit/secrets.toml` file inside the project directory:

```bash
mkdir -p .streamlit
nano .streamlit/secrets.toml
```

Paste your GROQ API key like this:

```toml
GROQ_API_KEY = "your_actual_groq_api_key_here"
```

Save the file.

### ✅ Step 4: Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
AlienGPT/
├── .streamlit/            # Contains secrets.toml for GROQ API key
│   └── secrets.toml
├── alien_data.json        # All alien species data
├── app.py                 # Main Streamlit application
├── prompts.py             # Prompt logic for generating alien-style replies
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

---

## 👽 Sample Aliens

- **Xarnok** – Plasma Being from Zephyria-9  
- **Vreeza** – Insectoid Dream Harvester  
- **Zibba** – Gelatinous Mood-Tech Inventor  
- **Grolf** – Rock Titan, Council Speaker  
- **K'thaal** – Time-folding Energy Wraith

---

## 💡 Future Enhancements

- Option to choose your alien species  
- Voice-based interaction (speech-to-text and text-to-speech)  
- Save and replay past conversations  
- Render custom alien avatars using AI

---

## 📜 License & Author

Created by [Jatin Garg]  
Powered by GROQ + LLaMA3
