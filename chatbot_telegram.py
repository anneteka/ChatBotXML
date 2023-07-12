import telebot

# t.me/XMLchat_bot
BOT_TOKEN = '6249367774:AAFOlNFVbE71oxVEnN-sE7B5b0V9zLAOj4Y'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Disclaimer: this bot is not a valid diagnostic instrument, however, you can use it to "
                          "evaluate your symptom and get useful information. "
                          "\n To start testing process use /testing command.")


@bot.message_handler(commands=['testing'])
def start_testing(message):
    print(message)
    bot.send_message(chat_id=message.chat.id, text="What symptoms do you currently experience?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# runs the bot
bot.infinity_polling()
