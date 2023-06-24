import telebot

# t.me/XMLchat_bot
BOT_TOKEN = '6249367774:AAFOlNFVbE71oxVEnN-sE7B5b0V9zLAOj4Y'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# runs the bot
bot.infinity_polling()
