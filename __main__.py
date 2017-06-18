import logging
from telegram import ParseMode
from telegram.ext import Updater, ConversationHandler, RegexHandler, CommandHandler
from keyboards import Keyboard as k
from text_data import Texts as t

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5, BRANCH6, BRANCH7 = range(8)
BRANCH1_1, BRANCH1_2, BRANCH1_3 = range(8, 11)
BRANCH2_1, BRANCH2_2, BRANCH2_3 = range(11, 14)
BRANCH3_1, BRANCH3_2, BRANCH3_3, BRANCH3_4 = range(14, 18)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def start(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.seven, parse_mode=ParseMode.MARKDOWN)
    return MENU

def br1(bot, update):
    return BRANCH1;

def br2(bot, update):
    return BRANCH2;

def menu(bot, update):
    update.message.reply_text(t.menu_text, reply_markup=k.seven, parse_mode=ParseMode.MARKDOWN)
    return MENU

def main():

    updater = Updater(token='383099020:AAG_L-5NahITmUTdJoYTSWMBX7n5561Pa8I')
    dispatcher = updater.dispatcher

    menu_conversation = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            MENU: [RegexHandler('^(1)$', br1), RegexHandler('^(2)$', br2),
                   RegexHandler('^(3)$', br3), RegexHandler('^(4)$', br4),
                   RegexHandler('^(5)$', br5), RegexHandler('^(6)$', br6),
                   RegexHandler('^(7)$', br7)],
        },

        fallbacks=[RegexHandler('^(Menu)$', menu)]
    )

    dispatcher.add_handler(menu_conversation)


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
