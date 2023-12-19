from collections import defaultdict

class ChatHandler:
    def __init__(self, max_size=None):
        self.conversations = defaultdict(list)
        self.max_size = max_size

    def add_message(self, chat_id, username, message):
        role = "assistant" if username is None else "user"
        self.conversations[chat_id].append({"role": role, "content": message})
        if self.max_size:
            self.conversations[chat_id] = self.conversations[chat_id][-self.max_size:]

        return self.conversations[chat_id]

    def get_conversation(self, chat_id):
        return self.conversations[chat_id]

    def clear_conversation(self, chat_id):
        self.conversations[chat_id] = []
