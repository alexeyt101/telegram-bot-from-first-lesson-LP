import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater('1225759745:AAGIvxdP49ci_1K4i4QjbS2oSyaZ217M-3c', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', green_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

def green_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text + ', джан'
    print(user_text)
    update.message.reply_text(user_text)


main()