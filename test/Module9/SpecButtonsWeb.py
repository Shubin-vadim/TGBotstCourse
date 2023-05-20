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

web_app_btn: KeyboardButton = KeyboardButton(
    text='Start web app',
    web_app=WebAppInfo(url='https://stepik.org/')
)


web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]], resize_keyboard=True
)


@dp.message(Command(commands=['web']))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Рубирика - эксперименты!',
        reply_markup=web_app_keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)