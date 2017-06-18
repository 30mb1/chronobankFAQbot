# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup

class Keyboard():
    one = ReplyKeyboardMarkup([['1'], ['Back⬅', 'Menu']], resize_keyboard=True)

    two = ReplyKeyboardMarkup([['1', '2'], ['Back⬅', 'Menu']], resize_keyboard=True)

    three = ReplyKeyboardMarkup([['1', '2', '3'], ['Back⬅', 'Menu']], resize_keyboard=True)

    four = ReplyKeyboardMarkup([['1', '2', '3', '4'], ['Back⬅', 'Menu']], resize_keyboard=True)

    five = ReplyKeyboardMarkup([['1', '2', '3', '4'], ['5', 'Back⬅', 'Menu']], resize_keyboard=True)

    six = ReplyKeyboardMarkup([['1', '2', '3', '4'], ['5', '6', 'Back⬅', 'Menu']], resize_keyboard=True)

    seven = ReplyKeyboardMarkup([['1', '2', '3', '4'], ['5', '6', '7']], resize_keyboard=True)
