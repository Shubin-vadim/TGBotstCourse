from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import (KeyboardButton, KeyboardButtonPollType, Message,
                           ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo

from aiogram.utils.keyboard import ReplyKeyboardBuilder


API_TOKEN: str = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
# contact_btn: KeyboardButton = KeyboardButton(
#                                 text='Отправить телефон',
#                                 request_contact=True)
# geo_btn: KeyboardButton = KeyboardButton(
#                                 text='Отправить геолокацию',
#                                 request_location=True)
# poll_btn: KeyboardButton = KeyboardButton(
#                                 text='Создать опрос/викторину',
#                                 request_poll=KeyboardButtonPollType())
#
# poll_btn2: KeyboardButton = KeyboardButton(
#     text='Создать опрос',
#     request_pooll=KeyboardButtonPollType(type='regular')
# )
#
# quiz_btn: KeyboardButton = KeyboardButton(
#     text='Создать викторину',
#     request_pooll=KeyboardButtonPollType(type='quiz')
# )
#
# # Добавляем кнопки в билдер
# # kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)
# kb_builder.row(poll_btn2, quiz_btn, width=1)
# # Создаем объект клавиатуры
# keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
#                                     resize_keyboard=True)


# Создаем кнопки
poll_btn_2: KeyboardButton = KeyboardButton(
                                text='Создать опрос',
                                request_poll=KeyboardButtonPollType(
                                                        type='regular'))

quiz_btn: KeyboardButton = KeyboardButton(
                                text='Создать викторину',
                                request_poll=KeyboardButtonPollType(
                                                        type='quiz'))

# Инициализируем билдер
poll_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер
poll_kb_builder.add(poll_btn_2, quiz_btn)

# Создаем объект клавиатуры
poll_keyboard: ReplyKeyboardMarkup = poll_kb_builder.as_markup(
                                        resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/poll"
@dp.message(Command(commands='poll'))
async def process_poll_command(message: Message):
    await message.answer(text='Экспериментируем с кнопками опрос/викторина',
                         reply_markup=poll_keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)