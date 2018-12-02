from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.constants import MAX_MESSAGE_LENGTH
import logging
import os
import subprocess

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'},
}

# export BOT_API_KEY=XXXXXXX,
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


def _process_user_input(text):
    if text != '':
        return ['ledger']+text.split(' ')[1:]


def run_ledger_command(bot, update):
    text = _process_user_input(update.message.text)
    try:
        result = subprocess.check_output(
            text,
            universal_newlines=True,
            # stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        result = 'Вы ввели не правильную команду.'

    if len(result) < MAX_MESSAGE_LENGTH:
        update.message.reply_text(result)
    else:
        update.message.reply_text('Ответ слишком длинный и не может быть выведен. Измените условия.')


if __name__ == '__main__':
    # ledger_bot = Updater(API_KEY)
    ledger_bot = Updater(API_KEY, request_kwargs=PROXY)
    dp = ledger_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("ledger", run_ledger_command))

    ledger_bot.start_polling()
    ledger_bot.idle()
