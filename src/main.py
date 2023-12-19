import os
import telebot
from utils.logger import logger
from utils.ai import ai_chat
from utils.utils import parse_message, info_menu
from utils.chat_handler import ChatHandler

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
chat_handler = ChatHandler()

@bot.message_handler(commands=['new'])
def new(message):
    logger.info('%s (%s) - started', message.from_user.id, message.from_user.username)
    chat_handler.clear_conversation(message.chat.id)
    bot.reply_to(message, f"Hi {message.from_user.first_name}! How can I help you?")

@bot.message_handler(commands=['start', 'help', 'info'])
def start(message):
    logger.info('%s (%s) - requested info', message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, info_menu, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def chat(message):
    logger.info('%s - %s (%s) - %s', message.chat.id, message.from_user.id, message.from_user.username, message.text)

    bot.send_chat_action(message.chat.id, "typing")

    conversation = chat_handler.add_message(message.chat.id, message.from_user.username, message.text)
    ollama_response = ai_chat(conversation)
    logger.info('Ollama response: ', ollama_response)

    reply_messages = parse_message(ollama_response)
    for reply_message in reply_messages:
        logger.info('%s - %s (%s) - %s', '-1', "jeeves", message.chat.id, message.from_user.id, message.from_user.username, reply_message)
        chat_handler.add_message(message.chat.id, None, reply_message)
        bot.reply_to(message, reply_message, parse_mode="Markdown")

bot.infinity_polling()
