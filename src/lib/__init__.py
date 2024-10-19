import os
from kink import di
from .logger import logger
from .chat_handler import ChatHandler
from .assistant_open import OpenAssistant
from .assistant_ollama import OllamaAssistant

di['logger'] = logger
di['bot_token'] = os.environ.get("BOT_TOKEN", "")
di['max_message_size'] = os.environ.get("MAX_MESSAGE_SIZE", 4096)

di['chat_handler'] = ChatHandler()

di['error_message'] = "I'm sorry, I couldn't understand that. Please try again."
di['info_menu'] = """
Introducing Jeeves, your trusty assistant bot!
Jeeves is here to help and assist you.

Here is the list of commands you can use:
- /new: Start a new conversation.
- /info: Display this info menu.

Note: Jeeves is an AI-powered bot and may not always provide accurate or up-to-date information. The answers provided by Jeeves are for informational purposes only and should not be relied upon as professional advice. It is important to verify any information obtained from Jeeves through other sources before making any decisions or taking any action. Additionally, Jeeves may not always be able to understand or respond to every request or question, so please be patient and try again if you do not receive a response. By using Jeeves, you acknowledge that you understand these limitations and will hold harmless the developers and owners of Jeeves in any case of inaccurate or incomplete information.
"""

if os.environ.get("PROFILE", "") == "ollama":
    di['ollama_model'] = os.environ.get("OLLAMA_MODEL", "")
    di['ollama_base_url'] = os.environ.get("OLLAMA_URL", "")
    di['assistant'] = OllamaAssistant()

else:
    di['open_model'] = os.environ.get("OPEN_MODEL", "")
    di['open_base_url'] = os.environ.get("OPEN_URL", "")
    di['open_api_key'] = os.environ.get("OPEN_API_KEY", "")
    di['assistant'] = OpenAssistant()
