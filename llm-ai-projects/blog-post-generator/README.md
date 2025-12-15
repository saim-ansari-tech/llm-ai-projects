# Blog Post Generator (LLM-based)

## Overview
This project is an AI-powered Blog Post Generator built using **Python**, **Streamlit**, and **OpenAI's GPT model 3.5 turbo**.  
It allows users to generate structured, SEO-friendly blog posts by simply providing a topic.

---

## Features
- AI-generated blog content with clear structure
- SEO-friendly and readable output
- Streamlit-based web interface
- Secure API key handling using environment variables
- Beginner-friendly and modular codebase

---

## Tech Stack
- Python
- Streamlit
- OpenAI API
- python-dotenv

---

## Project Structure
blog-post-generator/
│
├── app.py # Main application
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── .env.example # Environment variable template

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/llm-ai-projects.git
cd llm-ai-projects/blog-post-generator

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up environment variables
Create a .env file and add:
OPENAI_API_KEY=your_api_key_here

### 4. Run the application
streamlit run app.py


### Output
- Enter a blog topic
- The AI generates a complete blog with:
- Title
- Introduction
- Structured sections
- Conclusion 

### Security Note
- Never expose your API key
- .env files should not be committed to GitHub
- Use .env.example as a reference

###Author
Muhammad Saim Ansari
Robotics & AI Student
GitHub: https://github.com/saim-ansari-tech

---







