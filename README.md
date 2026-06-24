# 🚀 Scout AI

**Scout AI** is an AI-powered Startup Advisor inspired by the mentorship style of **Y Combinator**.

It helps aspiring founders move from a startup idea to a complete business blueprint by guiding them through:

* Startup Idea Generation
* Market Size Analysis
* TAM / SAM / SOM Estimation
* Competitor Research
* Revenue Model Design
* MVP Planning
* Go-To-Market Strategy
* Growth Strategy
* Elevator Pitch Creation

---

## ✨ Features

### 🤖 AI Startup Mentor

Scout AI acts as an experienced startup mentor and guides users through a structured workflow:

1. Understands:

   * Domain
   * Budget
   * Target Customers

2. Generates:

   * 5 Startup Ideas

3. Helps Analyze:

   * Problem Statement
   * Market Size
   * TAM / SAM / SOM
   * Competitor Analysis
   * Revenue Model
   * MVP Features
   * Risks
   * GTM Strategy
   * Growth Strategy
   * Elevator Pitch

---

## 🖥️ Available Interfaces

### 1. Streamlit Web Application

Modern web interface with:

* Dark Theme UI
* Interactive Chat Interface
* Conversation History
* Starter Suggestions
* Progress Tracker
* Real-time Streaming Responses

Run:

```bash
streamlit run app.py
```

---

### 2. CLI Application

Minimal terminal interface with streaming Gemini responses.

Run:

```bash
python main.py
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* Google Gemini API
* Google GenAI SDK

---

## 📂 Project Structure

```text
Scout-AI/

├── app.py                     # Streamlit App

├── main.py                    # CLI Version

├── prompts/
│   └── system_prompt.py

├── ui/
│   ├── styles.py
│   ├── sidebar.py
│   └── main_content.py

├── utils/
│   └── gemini_client.py

├── .env

├── requirements.txt

└── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/Rajasekhar-dotcom/ScoutAI.git

cd ScoutAI
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```env
api_key=YOUR_GEMINI_API_KEY
```

---

### 4. Run the Application

#### Streamlit Version

```bash
streamlit run app.py
```

#### CLI Version

```bash
python main.py
```

---

## Hosted website link
[Click here to check out Mr. Scout](https://scout-ai.streamlit.app)

---

## 🎯 Future Improvements

* PDF Export
* Startup Summary
* Pitch Deck Generator
* Save Conversations
* Multiple Startup Sessions
* Investor Pitch Evaluation
* Voice Interface

---

## 🌟 Inspiration

Scout AI is inspired by the mentorship philosophy of **Y Combinator**, focusing on helping founders think clearly, validate ideas, and build practical startup strategies.

---

## 👨‍💻 Author

**Rajasekhar Vedula**

Undergraduate Student | AI & ML Enthusiast | Builder

If you found this project interesting, consider giving it a ⭐ on GitHub.
