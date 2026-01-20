# ☁️ Cloud Infrastructure AI Assistant

An AI-powered assistant that helps users understand cloud infrastructure concepts and generate Azure CLI commands using natural language.

This project demonstrates how Generative AI can be integrated with cloud engineering workflows to provide architecture guidance, troubleshooting support, and infrastructure automation assistance.

---

## 🚀 Features

* Natural language cloud queries
* Azure infrastructure explanations
* Azure CLI command generation
* Prompt-engineered AI responses
* Modular and scalable Python architecture
* Secure API key handling using environment variables

---

## 🧠 How It Works

1. User enters a cloud-related question
2. System prompt defines the AI as a cloud engineer
3. Request is sent to a Large Language Model (LLM)
4. Model generates infrastructure-aware responses
5. Output is displayed in the terminal

---

## 🏗️ Architecture Overview

```
User Input
   ↓
Prompt Engineering (system + user prompt)
   ↓
LLM API (Groq – LLaMA 3.1)
   ↓
Generated Cloud Response
   ↓
Terminal Output
```

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **LLM Provider:** Groq (Free API)
* **Model:** LLaMA 3.1 8B Instant
* **Prompt Engineering**
* **GitHub Codespaces**
* **Virtual Environment (venv)**

---

## 📂 Project Structure

```
cloud-ai-assistant/
│
├── src/
│   ├── app.py          # Main application entry
│   ├── prompt.py       # System prompt instructions
│   └── ai_client.py    # LLM integration logic
│
├── .gitignore
├── requirements.txt
├── README.md
└── .env (not committed)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/jimishasurti/cloud-ai-assistant.git
cd cloud-ai-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

> ⚠️ The `.env` file is ignored by Git and never pushed to GitHub.

---

### 5️⃣ Run the Application

```bash
python src/app.py
```

---

## 💬 Example Prompts

* `Create an Azure VM with 2 CPUs and 8GB RAM`
* `Explain Azure VNET vs Subnet`
* `What is the difference between IaaS and PaaS?`
* `How to troubleshoot Azure VM connectivity issues`
* `Generate Azure CLI for storage account`

---

## 🔐 Security Best Practices

* API keys stored using environment variables
* `.env` excluded via `.gitignore`
* No secrets committed to repository

---

## 🌱 Future Enhancements

* Web UI using Streamlit
* Chat history and memory
* Azure OpenAI integration
* Deployment on Azure VM
* Docker containerization
* Logging and monitoring

---

## 👩‍💻 Author

**Jimishaa**
Cloud & Generative AI Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
