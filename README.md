# Terminal Chatbot

A simple command-line chatbot built with Python and the Google Gemini API.

## Features
- Chat with Gemini directly from the terminal
- Remembers the conversation (sends the full chat history with each request)
- Saves the conversation to `chat_history.json` on exit
- Handles lost internet connection without crashing

## Setup
```bash
git clone https://github.com/murtadha-alzubaidi/terminal-chatbot.git
cd terminal-chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your_api_key_here"
```

## Usage
```bash
python3 main.py
```
Type your message and press Enter. Type `exit` to quit and save the chat.

## What I Learned
- Calling an LLM API using `requests`
- Why LLMs have no memory, and how chat history solves it
- Saving data with JSON
