import logging
from telegram import ParseMode
from telegram.ext import Updater, ConversationHandler, RegexHandler, CommandHandler, MessageHandler, Filters
from keyboards import Keyboard as k
from text_data import Texts as t
import tree_scheme as b

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5, BRANCH6, BRANCH7 = range(8)
BRANCH1_1, BRANCH1_2, BRANCH1_3 = range(8, 11)
BRANCH2_1, BRANCH2_2, BRANCH2_3 = range(11, 14)
BRANCH3_1, BRANCH3_2, BRANCH3_3, BRANCH3_4 = range(14, 18)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def start(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    return MENU

def menu(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    return MENU

def main():

    updater = Updater(token='383099020:AAG_L-5NahITmUTdJoYTSWMBX7n5561Pa8I')
    dispatcher = updater.dispatcher

    menu_conversation = ConversationHandler(
        entry_points=[CommandHandler('start', start), MessageHandler(Filters.text, menu)],

        states={
            MENU: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                   RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                   RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                   RegexHandler('^(7)$', b.br7)],

            BRANCH1: [RegexHandler('^(1)$', b.br1_1), RegexHandler('^(2)$', b.br1_2),
                      RegexHandler('^(3)$', b.br1_3), RegexHandler('^(4)$', b.br1_4)],

            BRANCH2: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)],

            BRANCH3: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)],

            BRANCH4: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)],

            BRANCH5: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)],

            BRANCH6: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)],

            BRANCH7: [RegexHandler('^(1)$', b.br1), RegexHandler('^(2)$', b.br2),
                      RegexHandler('^(3)$', b.br3), RegexHandler('^(4)$', b.br4),
                      RegexHandler('^(5)$', b.br5), RegexHandler('^(6)$', b.br6),
                      RegexHandler('^(7)$', b.br7)]
        },

        fallbacks=[RegexHandler('^(Menu)$', menu)]
    )

    dispatcher.add_handler(menu_conversation)


    #updater.start_polling()
    updater.start_webhook(listen='104.131.182.147', port=8443,
                          url_path='383099020:AAG_L-5NahITmUTdJoYTSWMBX7n5561Pa8I',
                          key='/etc/letsencrypt/live/timebotserver.ml/privkey.pem',
                          cert='/etc/letsencrypt/live/timebotserver.ml/cert.pem',
                          webhook_url='https://timebotserver.ml:8443/383099020:AAG_L-5NahITmUTdJoYTSWMBX7n5561Pa8I')

    updater.bot.set_webhook(webhook_url='https://timebotserver.ml/383099020:AAG_L-5NahITmUTdJoYTSWMBX7n5561Pa8I',
                            certificate=open('/etc/letsencrypt/live/timebotserver.ml/cert.pem', 'rb'),
                            max_connections=100)

    updater.idle()

if __name__ == '__main__':
    main()
