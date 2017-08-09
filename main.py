import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echoes(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop = True)