# -*- coding: utf-8 -*-

import logging
from telegram import ParseMode
from telegram.ext import Updater, ConversationHandler, RegexHandler, CommandHandler, MessageHandler, Filters
from keyboards import Keyboard as k
from text_data import Texts as t
import branch1 as br1
import branch2 as br2
import branch3 as br3
import branch4 as br4
import branch5 as br5

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5 = range(6)
BRANCH2_1, BRANCH2_2, BRANCH2_3, BRANCH2_4 = range(6, 10)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def start(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    return MENU

def menu(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    return MENU

def br6(bot, update):
    update.message.reply_text(t.t6, reply_markup=k.menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    return MENU

def main():

    updater = Updater(token='403672400:AAHUXDp-qQ0irS6IHZlquDFzB8Ia8Ailc9A')
    dispatcher = updater.dispatcher

    menu_conversation = ConversationHandler(
        entry_points=[CommandHandler('start', start), MessageHandler(Filters.text, menu)],

        states={
            MENU: [RegexHandler('^(1)$', br1.m), RegexHandler('^(2)$', br2.m),
                   RegexHandler('^(3)$', br3.m), RegexHandler('^(4)$', br4.m),
                   RegexHandler('^(5)$', br5.m), RegexHandler('^(6)$', br6)],

            BRANCH1: [RegexHandler('^(1)$', br1.m_1), RegexHandler('^(2)$', br1.m_2),
                      RegexHandler('^(3)$', br1.m_3), RegexHandler('^(4)$', br1.m_4),
                      RegexHandler('^(5)$', br1.m_5)],

            BRANCH2: [RegexHandler('^(1)$', br2.m_1), RegexHandler('^(2)$', br2.m_2),
                      RegexHandler('^(3)$', br2.m_3), RegexHandler('^(4)$', br2.m_4)],

            BRANCH2_1: [RegexHandler('^(1)$', br2.m_1_1), RegexHandler('^(2)$', br2.m_1_2),
                       RegexHandler('^(3)$', br2.m_1_3), RegexHandler('^(4)$', br2.m_1_4),
                       RegexHandler('^(5)$', br2.m_1_5), RegexHandler('^(6)$', br2.m_1_6),
                       RegexHandler('^(7)$', br2.m_1_7), RegexHandler('^(Back)$', br2.back)],

            BRANCH2_2: [RegexHandler('^(1)$', br2.m_2_1), RegexHandler('^(2)$', br2.m_2_2),
                        RegexHandler('^(3)$', br2.m_2_3), RegexHandler('^(4)$', br2.m_2_4),
                        RegexHandler('^(Back)$', br2.back)],

            BRANCH2_3: [RegexHandler('^(1)$', br2.m_3_1), RegexHandler('^(2)$', br2.m_3_2),
                        RegexHandler('^(3)$', br2.m_3_3), RegexHandler('^(Back)$', br2.back)],

            BRANCH2_4: [RegexHandler('^(1)$', br2.m_4_1), RegexHandler('^(2)$', br2.m_4_2),
                        RegexHandler('^(3)$', br2.m_4_3), RegexHandler('^(4)$', br2.m_4_4),
                        RegexHandler('^(5)$', br2.m_4_5), RegexHandler('^(6)$', br2.m_4_6),
                        RegexHandler('^(7)$', br2.m_4_7), RegexHandler('^(8)$', br2.m_4_8),
                        RegexHandler('^(Back)$', br2.back)],

            BRANCH3: [RegexHandler('^(1)$', br3.m_1), RegexHandler('^(2)$', br3.m_2)],

            BRANCH4: [RegexHandler('^(1)$', br4.m_1), RegexHandler('^(2)$', br4.m_2)],

            BRANCH5: [RegexHandler('^(1)$', br5.m_1), RegexHandler('^(2)$', br5.m_2),
                      RegexHandler('^(3)$', br5.m_3), RegexHandler('^(4)$', br5.m_4),
                      RegexHandler('^(5)$', br5.m_5)],

        },

        fallbacks=[RegexHandler('^(Menu)$', menu)]
    )

    dispatcher.add_handler(menu_conversation)

    updater.bot.delete_webhook()
    #updater.start_polling()

    updater.bot.set_webhook(url='https://timebotserver.ml/403672400:AAHUXDp-qQ0irS6IHZlquDFzB8Ia8Ailc9A')
    updater.start_webhook(listen='127.0.0.1', port=5000, url_path='403672400:AAHUXDp-qQ0irS6IHZlquDFzB8Ia8Ailc9A')
    print updater.bot.get_webhook_info()
    updater.idle()

if __name__ == '__main__':
    main()
