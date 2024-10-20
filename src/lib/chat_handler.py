from collections import defaultdict
from kink import inject

@inject
class ChatHandler:
    def __init__(self, max_message_size, max_conversation_size=None):
        self.conversations = defaultdict(list)
        self.max_conversation_size = max_conversation_size
        self.max_message_size = max_message_size

    def add_message(self, chat_id, username, message):
        role = "assistant" if username is None else "user"
        self.conversations[chat_id].append({"role": role, "content": message})
        if self.max_conversation_size:
            self.conversations[chat_id] = self.conversations[chat_id][-self.max_conversation_size:]

        return self.conversations[chat_id]

    def get_conversation(self, chat_id):
        return self.conversations[chat_id]

    def clear_conversation(self, chat_id):
        self.conversations[chat_id] = []

    def parse_message(self, message):
        messages = []
        if len(message) < self.max_message_size:
            messages.append(message)
        else:
            for i in range(len(message) % self.max_message_size):
                messages.append(message[i*self.max_message_size:(i+1)*self.max_message_size])

        return messages