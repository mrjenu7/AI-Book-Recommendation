import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = ""

def recommend_books(genre, mood, goal):

    prompt = f"""
You are a book recommendation expert.

User Preferences:
Genre: {genre}
Mood: {mood}
Goal: {goal}

Suggest:
- 5 books
- Author names
- Why each book is suitable
- Who should read it
- Suggested reading order

Keep it simple and useful.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]