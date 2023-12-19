import os
import json
import requests

def ai_chat(conversation):
    data = {
        "model": os.environ.get("OLLAMA_MODEL"),
        "messages": conversation,
        "stream": False,
        "raw": True,
        "options": {
            "temperature": 0.2,
        },
    }

    response = requests.post(
        url=os.environ.get("OLLAMA_URL"),
        data=json.dumps(data),
        timeout=60*10,
    )
    response = response.json()["message"]["content"]
    return response
