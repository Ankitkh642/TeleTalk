from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from weather import weather

# check for new messages
updater = Updater(token="1146480644:AAFcm7wOmKm4c5tVkW7IT4AhDAt5JpKZE5I")

# allow to register handler like audio,video,text,gif
dispatcher = updater.dispatcher


# define a command callback function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat.id, text="""
    Hii ,I am your bot : Teletalk
    I can find the weather around you.To find your weather type /location .
    Otherwise I will repeat the message you send to me 
    So cool ! Right
    """)


# define  a command handler
start_handler = CommandHandler("start", start)

# add a  command handler to dispatch
dispatcher.add_handler(start_handler)


def get_location(bot, update):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id, text="Please Share Location", reply_markup=reply_markup)


get_location_handler = CommandHandler("location", get_location)
dispatcher.add_handler(get_location_handler)


def location(bot, update):
    lat = update.message.location.latitude
    long = update.message.location.longitude
    forecasts = weather.get_forecast(lat, long)
    bot.send_message(chat_id=update.message.chat_id, text=forecasts, reply_markup=ReplyKeyboardRemove())


location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)


# define a echo command
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


# define a echo handler
echo_handler = MessageHandler(Filters.text, echo)

# define a dispatcher for echo handler
dispatcher.add_handler(echo_handler)

# start polling
updater.start_polling()
