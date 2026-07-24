from flask import Flask
import telebot

TOKEN = "8600633783:AAEA7ZbrhLco3mU8Be5FILqHdXho9zPqkUU" 

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет!")

if __name__ == "__main__":
    bot.infinity_polling()
