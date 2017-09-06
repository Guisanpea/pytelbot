#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made with python 3
# pylint: disable=C1001
from telegram.ext import Updater, CommandHandler
from bot_actions import BotActions


def main():
    updater = Updater('TOKENSITO')
    updater.dispatcher.add_handler(CommandHandler('start', BotActions.start))
    updater.dispatcher.add_handler(CommandHandler('hola', BotActions.hola))
    updater.dispatcher.add_handler(CommandHandler('macho', BotActions.macho))
    updater.dispatcher.add_handler(CommandHandler('nudes', BotActions.send_memes))
    updater.dispatcher.add_handler(CommandHandler('ping', BotActions.ping))
    updater.dispatcher.add_handler(CommandHandler('id', BotActions.id))
    updater.dispatcher.add_error_handler(BotActions.show_error)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()