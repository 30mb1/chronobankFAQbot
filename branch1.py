from text_data import Texts as t
from keyboards import Keyboard as k
from telegram import ParseMode

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5 = range(6)
BRANCH2_1, BRANCH2_2, BRANCH2_3, BRANCH2_4 = range(6, 10)

def m(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.l2_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH1

def m_1(bot, update):
    update.message.reply_text(t.t1_1, reply_markup=k.l2_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH1

def m_2(bot, update):
    update.message.reply_text(t.t1_2, reply_markup=k.l2_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH1

def m_3(bot, update):
    update.message.reply_text(t.t1_3, reply_markup=k.l2_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH1
