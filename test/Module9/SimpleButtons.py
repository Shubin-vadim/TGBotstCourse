from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

API_TOKEN: str = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?', reply_markup=keyboard)


@dp.message(Text(text='Собак 🦮'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?') #reply_markup=ReplyKeyboardRemove())


@dp.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше') #reply_markup=ReplyKeyboardRemove())

if __name__ == '__main__':
    dp.run_polling(bot)