# 🛸 AlienGPT: Intergalactic Interview Simulator

AlienGPT is a fun and interactive AI project that simulates conversations with randomly generated alien beings. Each alien has a unique personality, background, and way of communicating. Great for fun chats, creative storytelling, or exploring unique perspectives.

---

## 🚀 Features

- 🌌 Random alien character generation from distant planets  
- 👽 Unique profiles including species, role, personality, and language quirks  
- 💬 Natural conversation styled with space-themed logic and language  
- 🧠 Alien responds from its unique point of view with curiosity and perspective  
- 🎨 Cool dark-themed UI built with Streamlit  
- ⚡ Powered by ""LLaMA-3"" via ""GROQ API""

---

## ⚙️ Installation & Usage

### ✅ Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/aliengpt.git
cd aliengpt
```

### ✅ Step 2: Install Requirements

Make sure you have Python 3.9+ installed, then install dependencies:

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Add Secrets

Create a `.streamlit/secrets.toml` file and paste your GROQ API key:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### ✅ Step 4: Run the App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
AlienGPT/
├── alien_data.json       # All alien species data
├── app.py                # Main Streamlit app
├── prompts.py            # Alien prompt generation logic
├── requirements.txt      # Python dependencies
└── README.md             # You're reading it
```

---

## 👽 Sample Alien Species

| Name     | Planet         | Role                    |
|----------|----------------|-------------------------|
| Xarnok   | Zephyria-9     | Quantum Philosopher     |
| Vreeza   | Nylax Prime    | Memory Harvester        |
| Zibba    | Jelloflux      | Mood-Tech Inventor      |
| Grolf    | Thargulon Beta | Council Speaker         |
| K'thaal  | Voidnest       | Archivist of Silent Stars|

---

## 💡 Ideas for Future

- 🌐 Add voice input & output
- 📸 Alien avatar/image generator
- 📁 Save & export conversation logs
- 🎛️ Choose alien by traits or planet

---

## 🧠 Credits & License

Made with 💻 by [Jatin Garg](https://github.com/yourprofile)  
Powered by [GROQ](https://groq.com/) + [LLaMA 3](https://ai.meta.com/llama/)  
