import os
import requests
import json
api_key = os.environ["GEMINI_API_KEY"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
headers = {"x-goog-api-key": api_key}

def ask(system, history):
    body = {
        "system_instruction": {"parts": [{"text": system}]},
        "contents": history
    }
    r = requests.post(url, headers=headers, json=body)
    if r.status_code == 200:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print(f"Error {r.status_code}: {r.text}")
        return None

system = "You are a helpful assistant. Answer briefly"
try:
    with open("chat_history.json","r") as f:
        history =json.load(f)
except FileNotFoundError:
    history = []
while True:
    question= input("You: ")
    if question=="exit":
        with open("chat_history.json","w")as f:
            json.dump(history,f,indent=4)
        print("Bye!")
        break
    if question=="":
        continue
    user_message = {"role": "user", "parts": [{"text": question}]}
    try:
        answer = ask(system, history + [user_message])
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        continue

    if answer is None:
        continue

    history.append(user_message)
    history.append({"role": "model", "parts": [{"text": answer}]})
    print("Bot:", answer)
