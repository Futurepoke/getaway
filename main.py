import logging
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler


TOKEN = os.environ.get('token')
PORT = int(os.environ.get('PORT', '8443'))


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://gettaway.herokuapp.com/" + TOKEN)
updater.idle()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='leaveit',
            input_message_content=InputTextMessageContent(inline_horvert(query))
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a useless bot, please kill me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()

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