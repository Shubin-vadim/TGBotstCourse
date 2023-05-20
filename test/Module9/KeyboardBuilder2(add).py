from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons1: list[KeyboardButton] = [KeyboardButton(
    text=f'Кнопка {i + 1}') for i in range(3)
]

kb_builder.row(*buttons1, width=4)

buttons2: list[KeyboardButton] = [KeyboardButton(
    text=f'Кнопка {i + 6}') for i in range(10)
]


kb_builder.add(*buttons2)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=True))

if __name__ == '__main__':
    dp.run_polling(bot)