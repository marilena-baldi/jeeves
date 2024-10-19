import json
import requests
from kink import inject

@inject
class OpenAssistant:
    def __init__(self, open_api_key, open_model, open_base_url, logger):
        self.api_key = open_api_key
        self.model = open_model
        self.base_url = open_base_url
        self.logger = logger

    def chat(self, messaages):
        data = {
            "model": self.model,
            "messages": messaages,
            "temperature": 0.2,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(
            url=self.base_url,
            headers=headers,
            data=json.dumps(data),
            timeout=60,
        )
        response = response.json().get("choices", [])[0].get("message", {}).get("content", "")
        self.logger.debug("Assistant response: %s", response)

        return response
