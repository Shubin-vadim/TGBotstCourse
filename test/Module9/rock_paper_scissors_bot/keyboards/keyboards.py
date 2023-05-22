from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from test.Module9.rock_paper_scissors_bot.lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

btn_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
btn_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(btn_yes, btn_no, width=2)


yes_no_kb = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

btn_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
btn_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
btn_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[btn_1],
              [btn_2],
              [btn_3]],
    resize_keyboard=True
)
