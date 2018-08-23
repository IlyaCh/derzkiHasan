#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from uuid import uuid4

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Я дерзкий Хасан! Я научу тебя материться в стиле "пьяный Хасан". В моей базе дохера сценариев как можно материться. Используй /help чтобы узнать больше.')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Пошли кого-нибудь, используй обращение "@derzkihasanBot  ". Можно использовать в любом чате с любым человеком. Пока доступно мало сценариев из глоссария Хасана. Новые цитаты буду добавляться по мере поступления.')
 
def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    
    arr=["на хую вертел я блять твое мнение", "да ебись ты в рот хуй собачий", \
          "Ублюдок, мать твою, а ну иди сюда говно собачье, решил ко мне лезть? Ты, засранец вонючий, мать твою, а? Ну иди сюда, попробуй меня трахнуть, я тебя сам трахну ублюдок, онанист чертов, будь ты проклят, иди идиот, трахать тебя и всю семью, говно собачье, жлоб вонючий, дерьмо, сука, падла, иди сюда, мерзавец, негодяй, гад, иди сюда ты - говно, ЖОПА!"]
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Мнение",
            input_message_content=InputTextMessageContent(arr[0])),            
        InlineQueryResultArticle(
            id=uuid4(),
            title="Ебись",
            input_message_content=InputTextMessageContent(arr[1])),
        InlineQueryResultArticle(
            id=uuid4(),
            title="А ну иди сюда...",
            input_message_content=InputTextMessageContent(arr[2]))]

    update.inline_query.answer(results)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    TOKEN='604574445:AAE38v8M0Imgx8xQF_GwWoKqSynyF2PZhI0'
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()