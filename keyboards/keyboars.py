from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import lexicon_ru

yes_no_kb_builder = ReplyKeyboardBuilder()

button_yes = KeyboardButton(text = lexicon_ru['yes_button'])
button_no = KeyboardButton(text = lexicon_ru['no_button'])

yes_no_kb_builder.row(button_yes, button_no, width = 2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

button_rock = KeyboardButton(text =lexicon_ru['rock'])
button_paper = KeyboardButton(text = lexicon_ru['paper'])
button_scissors = KeyboardButton(text=lexicon_ru['scissors'])

game_kb = ReplyKeyboardMarkup(
    keyboard = [
        [button_paper],
        [button_rock],
        [button_scissors],
    ], resize_keyboard=True
)