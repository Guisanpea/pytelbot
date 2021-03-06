#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made with python 2
# pylint: disable=C1001
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot_actions import BotActions
from message_filter import *


def main():
    json_config = open("tokens.json", 'r')
    tokens = json.load(json_config)
    json_config.close()
    updater = Updater(tokens["telegram"])
    happy_filter = HappyFilter()
    unhappy_filter = NotHappyFilter()
    insulto_filter = Insulto()
    easy_filter = EasyReact()
    pasa_filter = CuandoTePasaReact()
    botijo = BotijoReaction()
    thicc = Thicc()
    spain_filter = BuenosDias()
    reverte_filter = ReverteReact()
    reverted_filter = RevertedReact()
    sad_filter = SadReacts()
    gracias_filter = Gracias()
    xd = Xdd()
    # TODO
    # gracias = Gracias()
    # habeces = AVeces()
    updater.dispatcher.add_handler(CommandHandler('start', BotActions.start))
    updater.dispatcher.add_handler(CommandHandler('hola', BotActions.hola))
    updater.dispatcher.add_handler(CommandHandler('macho', BotActions.macho))
    updater.dispatcher.add_handler(CommandHandler('nudes', BotActions.send_memes))
    updater.dispatcher.add_handler(CommandHandler('ping', BotActions.ping))
    updater.dispatcher.add_handler(CommandHandler('id', BotActions.id_user))
    updater.dispatcher.add_handler(CommandHandler('id_c', BotActions.id_chat))
    updater.dispatcher.add_handler(CommandHandler('help', BotActions.help))
    updater.dispatcher.add_handler(CommandHandler('animals', BotActions.animals))
    updater.dispatcher.add_handler(CommandHandler('tweet', BotActions.tweet))
    updater.dispatcher.add_handler(CommandHandler('sad', BotActions.sad_reacts))
    updater.dispatcher.add_handler(CommandHandler('search', BotActions.search))
    updater.dispatcher.add_handler(CommandHandler('pole', BotActions.pole))
    updater.dispatcher.add_handler(CommandHandler('porro', BotActions.hora_porro))
    updater.dispatcher.add_handler(CommandHandler('pi', BotActions.horacio_pi))
    updater.dispatcher.add_handler(CommandHandler('comunist', BotActions.comunist_meme))
    updater.dispatcher.add_handler(CommandHandler('set_tw_acc', BotActions.add_twitter_account))
    updater.dispatcher.add_handler(CommandHandler('info', BotActions.info_user_group))
    updater.dispatcher.add_handler(CommandHandler('twitter_acc', BotActions.send_twitter_acc))
    updater.dispatcher.add_handler(CommandHandler('current_status', BotActions.current_status))
    updater.dispatcher.add_handler(MessageHandler(happy_filter, BotActions.happy))
    updater.dispatcher.add_handler(MessageHandler(unhappy_filter, BotActions.not_happy))
    updater.dispatcher.add_handler(MessageHandler(botijo, BotActions.botijo_react))
    updater.dispatcher.add_handler(MessageHandler(insulto_filter, BotActions.insulto_method))
    updater.dispatcher.add_handler(MessageHandler(easy_filter, BotActions.easy_command))
    updater.dispatcher.add_handler(MessageHandler(pasa_filter, BotActions.when_te_pasa))
    updater.dispatcher.add_handler(MessageHandler(gracias_filter, BotActions.graciasReact))
    updater.dispatcher.add_handler(MessageHandler(thicc, BotActions.thicc))
    updater.dispatcher.add_handler(MessageHandler(spain_filter, BotActions.spain))
    updater.dispatcher.add_handler(MessageHandler(reverte_filter, BotActions.reverte))
    updater.dispatcher.add_handler(MessageHandler(reverted_filter, BotActions.reverted))
    updater.dispatcher.add_handler(MessageHandler(sad_filter, BotActions.sad))
    updater.dispatcher.add_handler(MessageHandler(xd, BotActions.xd_react))
    # TODO
    # updater.dispatcher.add_handler(MessageHandler(gracias, BotActions.gracias))
    # updater.dispatcher.add_handler(MessageHandler(habeces, BotActions.habeces))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, BotActions.mensajes_callback))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
