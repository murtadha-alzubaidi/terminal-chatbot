import os
import requests

api_key = os.environ["GEMINI_API_KEY"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
headers = {"x-goog-api-key": api_key}

def ask(system, question):
    body = {
        "system_instruction": {"parts": [{"text": system}]},
        "contents": [{"parts": [{"text": question}]}]
    }
    r = requests.post(url, headers=headers, json=body)
    if r.status_code == 200:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error {r.status_code}: {r.text}"

system = "You are a helpful assistant. Answer briefly"
while True:
    question= input("You: ")
    if question=="exit":
        print("Bye!")
        break
    if question=="":
        continue
    try:
        answer= ask(system,question)
        print("Bot:", answer)
    except requests.exceptions.ConnectionError:
        print("no internet connection")
