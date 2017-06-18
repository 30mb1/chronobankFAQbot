from text_data import Texts as t
from keyboards import Keyboard as k
from telegram import ParseMode

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5 = range(6)
BRANCH2_1, BRANCH2_2, BRANCH2_3, BRANCH2_4 = range(6, 10)

def back(bot, update):
    update.message.reply_text(t.t2, reply_markup=k.l2_four, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2

def m(bot, update):
    update.message.reply_text(t.t2, reply_markup=k.l2_four, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2

def m_1(bot, update):
    update.message.reply_text(t.t2_1, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_1(bot, update):
    update.message.reply_text(t.t2_1_1, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_2(bot, update):
    update.message.reply_text(t.t2_1_2, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_3(bot, update):
    update.message.reply_text(t.t2_1_3, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_4(bot, update):
    update.message.reply_text(t.t2_1_4, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_5(bot, update):
    update.message.reply_text(t.t2_1_5, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_6(bot, update):
    update.message.reply_text(t.t2_1_6, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_1_7(bot, update):
    update.message.reply_text(t.t2_1_7, reply_markup=k.l3_seven, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_1

def m_2(bot, update):
    update.message.reply_text(t.t2_2, reply_markup=k.l3_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_2

def m_2_1(bot, update):
    update.message.reply_text(t.t2_2_1, reply_markup=k.l3_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_2

def m_2_2(bot, update):
    update.message.reply_text(t.t2_2_2, reply_markup=k.l3_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_2

def m_2_3(bot, update):
    update.message.reply_text(t.t2_2_3, reply_markup=k.l3_three, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_2

def m_3(bot, update):
    update.message.reply_text(t.t2_3, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_1(bot, update):
    update.message.reply_text(t.t2_3_1, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_2(bot, update):
    update.message.reply_text(t.t2_3_2, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_3(bot, update):
    update.message.reply_text(t.t2_3_3, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_4(bot, update):
    update.message.reply_text(t.t2_3_4, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_5(bot, update):
    update.message.reply_text(t.t2_3_5, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_3_6(bot, update):
    update.message.reply_text(t.t2_3_6, reply_markup=k.l3_six, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_3

def m_4(bot, update):
    update.message.reply_text(t.t2_4, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_1(bot, update):
    update.message.reply_text(t.t2_4_1, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_2(bot, update):
    update.message.reply_text(t.t2_4_2, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_3(bot, update):
    update.message.reply_text(t.t2_4_3, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_4(bot, update):
    update.message.reply_text(t.t2_4_4, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_5(bot, update):
    update.message.reply_text(t.t2_4_5, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_6(bot, update):
    update.message.reply_text(t.t2_4_6, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_7(bot, update):
    update.message.reply_text(t.t2_4_7, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_8(bot, update):
    update.message.reply_text(t.t2_4_8, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4

def m_4_9(bot, update):
    update.message.reply_text(t.t2_4_9, reply_markup=k.l3_nine, parse_mode=ParseMode.MARKDOWN)
    return BRANCH2_4
