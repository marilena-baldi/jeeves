import telebot
from lib import di

bot = telebot.TeleBot(di['bot_token'])
chat_handler = di['chat_handler']
assistant = di['assistant']
logger = di['logger']
info_menu = di['info_menu']
error_message = di['error_message']


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
    response = assistant.chat(conversation)

    reply_messages = chat_handler.parse_message(response) if response else [error_message]
    for reply_message in reply_messages:
        logger.info('%s - %s (%s) - %s', message.chat.id, "-1", "jeeves", reply_message)
        chat_handler.add_message(message.chat.id, None, reply_message)
        bot.send_message(message.chat.id, reply_message)

bot.infinity_polling()
