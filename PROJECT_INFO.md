# Debales AI Assistant (LangGraph + RAG)

A smart AI chatbot built using Python, LangGraph, LangChain, and RAG (Retrieval-Augmented Generation).

This assistant can:
- Answer questions related to Debales AI using scraped website data
- Use SERP API for external/general queries
- Route queries intelligently using LangGraph
- Avoid hallucinations using retrieved context

## Features

- RAG-based chatbot
- SERP API integration
- LangGraph workflow routing
- Website scraping with BeautifulSoup
- Vector database using FAISS
- Simple CLI interaction
- Clean and modular project structure

## Technologies Used

- Python
- LangChain
- LangGraph
- OpenAI
- FAISS
- BeautifulSoup
- SERP API

## How to Run

1. Run scraper:
python scraper.py

2. Create vector database:
python rag.py

3. Start chatbot:
python app.py

## Example Questions

- What is Debales AI?
- What integrations does Debales AI support?
- Who is Elon Musk?
- Latest AI news

## Project Structure

debales_ai_bot/
│
├── app.py
├── graph.py
├── rag.py
├── scraper.py
├── tools.py
├── requirements.txt
├── README.md
└── .env.example
