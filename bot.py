import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings


logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def greet_user(update, context):
    print('Вызвана команда /start')
    update.message.reply_text('Здравствуй, пользователь! Ты вызвал команду /start')
    print(update)


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('BOT STARTED')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

"""
> между блоками без отступа (например, функциями) принято ставить по две пустые строки
То есть все предыдущие задания хорошо бы тоже переписать в соответсвии с этим и делать так везде?
"""