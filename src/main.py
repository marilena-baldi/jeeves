from lib import di

bot_handler = di['bot_handler']
bot = bot_handler.bot

@bot.message_handler(commands=['new'])
def new(message):
    bot_handler.new(message)

@bot.message_handler(commands=['start', 'help', 'info'])
def start(message):
    bot_handler.start(message)

@bot.message_handler(func=lambda message: True)
def chat(message):
    bot_handler.chat(message)

bot.infinity_polling()
