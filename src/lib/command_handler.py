import telebot
from kink import inject
import subprocess

@inject
class CommandHandler:
    def __init__(self, bot_token, logger, chat_handler, assistant,
                 start_message, error_message, info_menu, host_name, host_password):
        self.bot = telebot.TeleBot(bot_token)
        self.logger = logger
        self.chat_handler = chat_handler
        self.assistant = assistant
        self.start_message = start_message
        self.error_message = error_message
        self.info_menu = info_menu
        self.host_name = host_name
        self.host_password = host_password

    def new(self, message):
        self.logger.info('%s (%s) - started', message.from_user.id, message.from_user.username)

        self.chat_handler.clear_conversation(message.chat.id)
        self.bot.reply_to(message, self.start_message.format(username=message.from_user.first_name))

    def start(self, message):
        self.logger.info('%s (%s) - requested info', message.from_user.id, message.from_user.username)

        self.bot.send_message(message.chat.id, self.info_menu, parse_mode="Markdown")

    def shutdown(self, message):
        self.logger.info('%s (%s) - shut down', message.from_user.id, message.from_user.username)

        subprocess.run([
                "sshpass", "-p", self.host_password,
                "ssh", "-o", "StrictHostKeyChecking=no", f"{self.host_name}@localhost", "sudo", "shutdown", "now",
        ])

    def chat(self, message):
        self.logger.info('%s - %s (%s) - %s', message.chat.id, message.from_user.id, message.from_user.username, message.text)

        self.bot.send_chat_action(message.chat.id, "typing")

        conversation = self.chat_handler.add_message(message.chat.id, message.from_user.username, message.text)
        response = self.assistant.chat(conversation)
        reply_messages = self.chat_handler.parse_message(response) if response else [self.error_message]
        for reply_message in reply_messages:
            self.logger.info('%s - %s (%s) - %s', message.chat.id, "-1", "jeeves", reply_message)

            self.chat_handler.add_message(message.chat.id, None, reply_message)
            self.bot.send_message(message.chat.id, reply_message)
