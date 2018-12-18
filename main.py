import telebot
import os
from telebot import types

bot = telebot.TeleBot(os.environ.get('token'))

def horvert(input):
    horizon = ''
    for i in input.text:
        horizon += i
        horizon += "   "
    vertirizon = ''
    for i in input.text[1:]:
        vertirizon += i
        vertirizon += "\n"
    return horizon + "\n" + vertirizon

def inline_horvert(input):
    horizon = ''
    for i in input:
        horizon += i
        horizon += "   "
    vertirizon = ''
    for i in input[1:]:
        vertirizon += i
        vertirizon += "\n"
    return horizon + "\n" + vertirizon

@bot.message_handler(content_types=["text"])
def echoes(message):
    try:
        bot.send_message(message.chat.id, horvert(message))
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query )
def query_text(inline_query):
    try:
        result = inline_horvert(inline_query.query)
        r = types.InlineQueryResultArticle('2', 'Process text', types.InputTextMessageContent(result))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop = True)