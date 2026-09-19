# 🤖 pyBusinessInquiryBot

### 💬 A Business Inquiry Chatbot Built with Python

> 🌱 **A beginner-friendly Python chatbot that answers common business questions using simple rule-based responses and structured business data.**

**AI by Aryan** is a fictional business used as the data source for this project.

---

## ✨ What is this?

**Business Inquiry Bot** is a Python-based command-line chatbot designed to handle common customer inquiries about a business.

Instead of hardcoding everything into one file, the project separates:

- 💬 Chat interface
- 🧠 Bot response logic
- 🏢 Business information

This makes the project easier to understand, maintain, and expand.

---

##  Features

| Feature | Description |
|---|---|
| 👋 Greetings | Responds to basic greetings |
| 🏢 Business Info | Provides business information |
| 👨‍💻 Founder Info | Gives founder/owner information |
| 📍 Location | Provides business address |
| 📞 Contact | Provides phone, email and website |
| 🕐 Business Hours | Shows working hours |
| 💰 Pricing | Provides service pricing |
| 🛠️ Services | Lists available services |
| 📖 About | Explains the business |
| 🌐 Social Media | Provides social media information |
| ❓ FAQ | Provides frequently asked questions |
| 🚪 Exit | Allows the user to leave the chatbot |
| 🛟 Fallback | Handles questions the bot doesn't recognize |

---

## 🧠 How It Works

The chatbot currently uses **rule-based keyword matching**.

```text
                👤 User
                  │
                  ▼
             💬 User Input
                  │
                  ▼
          🧠 Keyword Detection
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Services   Pricing   Contact
        │         │         │
        └─────────┼─────────┘
                  ▼
          🏢 Business Data
                  │
                  ▼
            🤖 Bot Response
                  │
                  ▼
                👤 User
```

For example:

```text
You: What services do you provide?

Bot: We provide:
     AI Chatbot Development
     Business Automation
     Machine Learning Solutions
     ...
```

The bot reads the user's message, checks for relevant keywords, and retrieves the appropriate information from the business data.

---

## 📂 Project Structure

```text
pyBusinessInquiryBot/
│
├── 📄 index.py
│   └── Main chatbot interface
│
├── 🧠 botResponses.py
│   └── Chatbot response and keyword logic
│
├── 🏢 businessData.py
│   └── Business information and data
│
└── 📖 README.md
    └── Project documentation
```

### 🔗 How the files communicate

```text
index.py
   │
   │ calls
   ▼
botResponses.py
   │
   │ reads
   ▼
businessData.py
```

This separation keeps the chatbot logic and business information independent.

---

## 🏢 Mock Business

The chatbot currently uses a fictional company:

### ✨ AI by Aryan

**Tagline:**  
> Smart AI Solutions for Modern Businesses

### 💼 Business Type

AI & Technology Solutions

### 🛠️ Example Services

- 🤖 AI Chatbot Development
- ⚙️ Business Automation
- 🧠 Machine Learning Solutions
- 🌐 AI Website Integration
- 📊 Data Analysis
- 💡 Custom AI Applications

> ⚠️ **Note:** AI by Aryan is fictional mock data created for this learning project.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-gour127/pyBusinessInquiryBot.git
```

### 2️⃣ Move into the project

```bash
cd pyBusinessInquiryBot
```

### 3️⃣ Run the chatbot

```bash
python index.py
```

---

## 💬 Example Conversation

```text
====================================
      AI BY ARYAN - BUSINESS BOT
====================================

You: hello

Bot: Hello! 👋 Welcome to AI by Aryan.
How can I help you today?

You: what services do you provide?

Bot: We provide:
AI Chatbot Development
Business Automation
Machine Learning Solutions
AI Website Integration
Data Analysis
Custom AI Applications

You: where are you located?

Bot: We are located at:
Tech Park, Innovation Avenue,
Nagpur, Maharashtra, India

You: what is your phone number?

Bot: You can contact us through:
Phone: +91 98765 43210
Email: hello@aibyryan.example
Website: https://aibyryan.example

You: bye

Bot: Thank you for visiting AI by Aryan! 👋
```

---

## 🧩 Technologies Used

```text
🐍 Python
📦 Python Modules
🔤 String Processing
🔀 Conditional Logic
📚 Lists
🗂️ Dictionaries
🔁 Loops
🧠 Rule-Based Logic
```

No external libraries are required for the current version.

---

## 🎯 Learning Goals

This project was created to practice important Python concepts through a small real-world-style application.

### Concepts practiced

- Python functions
- `if / elif / else`
- Lists
- Dictionaries
- String manipulation
- `any()`
- Loops
- Module imports
- Separating data from logic
- User input
- Basic chatbot architecture

---

## 🛣️ Future Roadmap

This project is intentionally starting simple.

The goal is to gradually turn the basic chatbot into a more intelligent business assistant.

```text
🌱 V1
Rule-Based Chatbot
      ↓
📦 V2
JSON Business Data
      ↓
🏗️ V3
Object-Oriented Design
      ↓
🧠 V4
Better Intent Detection
      ↓
🔤 V5
NLP
      ↓
🤖 V6
ML Intent Classification
      ↓
🔎 V7
Semantic Search
      ↓
📚 V8
RAG
      ↓
✨ V9
LLM-Powered Business Assistant
      ↓
🌐 V10
Web / API Application
```

---

## 💡 Why I Built This

This project is part of my journey of learning Python and gradually moving toward **AI/ML development**.

Rather than jumping directly into complex AI frameworks, I wanted to understand how a chatbot works at the fundamental level first.

The project will be improved step-by-step as I learn more about:

**Python → OOP → NLP → Machine Learning → AI**

---

## 🐛 Current Limitations

The current chatbot is intentionally simple.

It relies on keyword matching, so it may not understand:

- Complex sentences
- Different ways of asking the same question
- Context between multiple messages
- Questions outside its predefined business information

These limitations are part of the learning process and provide the foundation for future NLP/ML improvements.

---

## 🌱 Future Vision

The long-term goal is to transform this:

```text
if keyword in message:
    return response
```

into something closer to:

```text
User
 ↓
Natural Language Processing
 ↓
Intent Detection
 ↓
Business Knowledge Retrieval
 ↓
Context Understanding
 ↓
Intelligent Response
```

---

## 👨‍💻 Author

### Aryan Gour

B.Tech Artificial Intelligence Student  
Python • Web Development

🐙 **GitHub:**  
https://github.com/Aryan-gour127

---

## ⭐ Support

If you like this project, consider giving the repository a ⭐

It helps motivate me to keep building and learning! 🚀

---

### 💙 Built with Python & curiosity

> *Start simple. Understand the fundamentals. Build bigger.* 🐍✨
