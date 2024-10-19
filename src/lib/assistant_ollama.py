import json
import requests
from kink import inject

@inject
class OllamaAssistant:
    def __init__(self, ollama_model, ollama_base_url, logger):
        self.model = ollama_model
        self.base_url = ollama_base_url
        self.logger = logger

    def chat(self, messaages):
        data = {
            "model": self.model,
            "messages": messaages,
            "stream": False,
            "raw": True,
            "options": {
                "temperature": 0.2,
            },
        }

        response = requests.post(
            url=self.base_url,
            data=json.dumps(data),
            timeout=600,
        )
        response = response.json().get("message", {}).get("content", "")
        self.logger.debug("Assistant response: %s", response)

        return response
