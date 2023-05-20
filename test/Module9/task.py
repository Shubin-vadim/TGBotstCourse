from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append(KeyboardButton(text='7'))

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)

kb_builder.row(*keyboard, width=1)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=my_keyboard))

if __name__ == '__main__':
    dp.run_polling(bot)