import telebot
from prepare.telegram import process_telegram_message

# t.me/XMLchat_bot

# token is used to identify a telegram bot
BOT_TOKEN = '6249367774:AAFOlNFVbE71oxVEnN-sE7B5b0V9zLAOj4Y'

bot = telebot.TeleBot(BOT_TOKEN)


# handles user sending a /start or /hello command
# responds with a greetings message and nullifies user testing data
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Disclaimer: this bot is not a valid diagnostic instrument, however, you can use it to "
                          "evaluate your symptom and get useful information. "
                          "\nTo start testing process use /testing command."
                          "\nIf you wish to delete your data simply restart the bot.")
    process_telegram_message.setup_user(message.chat.id)


# handles user sending a /testing command
# starts user testing
@bot.message_handler(commands=['testing'])
def start_testing(message):
    bot.send_message(chat_id=message.chat.id, text="What symptoms do you currently experience?")
    process_telegram_message.start_testing(user_id=message.chat.id)


# handles any incoming user messages
@bot.message_handler(func=lambda msg: True)
def process_all(message):
    bot.send_message(chat_id=message.chat.id,
                     text=process_telegram_message.process_general_message(message.chat.id, message.text))


# runs the bot
bot.infinity_polling()
