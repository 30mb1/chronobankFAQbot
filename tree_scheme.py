from keyboards import Keyboard as k
from text_data import Texts as t

MENU, BRANCH1, BRANCH2, BRANCH3, BRANCH4, BRANCH5, BRANCH6, BRANCH7 = range(8)
BRANCH1_1, BRANCH1_2, BRANCH1_3 = range(8, 11)
BRANCH2_1, BRANCH2_2, BRANCH2_3 = range(11, 14)
BRANCH3_1, BRANCH3_2, BRANCH3_3, BRANCH3_4 = range(14, 18)

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.l2_four)
    return BRANCH1

def br2(bot, update):
    update.message.reply_text(t.t2, reply_markup=k.l2_four)
    return BRANCH2

def br3(bot, update):
    update.message.reply_text(t.t3, reply_markup=k.l2_four)
    return BRANCH3

def br4(bot, update):
    update.message.reply_text(t.t4, reply_markup=k.l2_two)
    return BRANCH4

def br5(bot, update):
    update.message.reply_text(t.t5, reply_markup=k.l2_three)
    return BRANCH5

def br6(bot, update):
    update.message.reply_text(t.t6, reply_markup=k.l2_seven)
    return BRANCH6

#end of branch
def br7(bot, update):
    update.message.reply_text(t.t7, reply_markup=k.menu_keyboard)
    return MENU

def br1_1(bot, update):
    update.message.reply_text(t.t1_1, reply_markup=k.l3_three)
    return BRANCH1_1

def br1_2(bot, update):
    update.message.reply_text(t.t1_2, reply_markup=k.l3_three)
    return BRANCH1_2

def br1_3(bot, update):
    update.message.reply_text(t.t1_3, reply_markup=k.l3_three)
    return BRANCH1_3

#end of branch
def br1_4(bot, update):
    update.message.reply_text(t.t1_4, reply_markup=k.l2_four)
    return BRANCH1
'''
def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1

def br1(bot, update):
    update.message.reply_text(t.t1, reply_markup=k.five)
    return BRANCH1'''
