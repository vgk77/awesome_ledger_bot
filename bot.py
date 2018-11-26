from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

API_KEY = os.environ['BOT_API_KEY']

logging.basicConfig(
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greet_user(bot, update):
    text = 'testtext'
    print(text)
    update.message.reply_text(text)


def get_ledger_balance():
    pass


def main():
    ledger_bot = Updater(API_KEY)

    dp = ledger_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("bal", get_ledger_balance))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    ledger_bot.start_polling()
    ledger_bot.idle()

main()