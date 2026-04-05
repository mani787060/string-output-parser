# LangChain String Output Parser
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://www.langchain.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Model-Google%20Gemini-4285F4)](https://ai.google.dev/)

## 🏗️ Project Overview
This repository demonstrates the use of the **`StrOutputParser`**, the most commonly used output parser in the LangChain ecosystem. By default, LLMs return a complex object containing the response text, usage statistics, and metadata. This project showcases how to use a parser to "sink" that complexity and retrieve only the clean, final string—making the output ready for display or further text processing.

---

## 🛠️ Key Technical Implementations

### 1. LCEL Chain Integration
* **Pipeline Flow:** Implementing the `|` (pipe) operator to create a seamless data flow: `PromptTemplate | ChatModel | StrOutputParser`.
* **Output Normalization:** Ensuring that regardless of the model used (OpenAI, Gemini, etc.), the final output is always a simple Python string.

### 2. Handling Streamed Content
* **Chunk Extraction:** Demonstrating how `StrOutputParser` handles streamed chunks, allowing for real-time UI updates without manual string concatenation.

### 3. Developer Productivity
* **Code Cleanliness:** Reducing boilerplate code by replacing manual `response.content` calls with a standardized parser in the chain definition.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **Orchestration:** LangChain (`langchain-core`, `langchain-google-genai`)
* **Model:** Google Gemini Pro
* **Environment:** `python-dotenv`

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/langchain-string-output-parser.git](https://github.com/your-username/langchain-string-output-parser.git)

2. **Install Dependencies:**
   ```bash
   pip install -U langchain-core langchain-google-genai python-dotenv

3. **Setup API Key:**
Create a .env file in the root directory:
   ```bash
   GOOGLE_API_KEY=your_gemini_key_here

4. **Run the Implementation:**
   ```bash
   python string_0utput_parser.py   
