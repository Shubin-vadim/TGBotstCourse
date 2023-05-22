from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.filters import CommandStart

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


url_btn1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс "Телеграм-боты" на Python и AIOgram',
    url='https://stepik.org/120924'
)

url_btn2: InlineKeyboardButton = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)

group_name = 'aiogram_stepik_course'
user_id = 173901673
channel_name = 'toBeAnMLspecialist'

url_btn3: InlineKeyboardButton = InlineKeyboardButton(
    text='Группа телеграм-боты на AIOgram',
    url=f'tg://resolve?domain={group_name}'
)

url_btn4: InlineKeyboardButton = InlineKeyboardButton(
    text='Автор курса по телеграм-ботам',
    url=f'tg://user?id={user_id}'
)

url_btn5: InlineKeyboardButton = InlineKeyboardButton(
    text='Канал по ML',
    url=f'https://t.me/{channel_name}'
)

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_btn1],
                     [url_btn2],
                     [url_btn3],
                     # [url_btn4],
                     [url_btn5]]
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопка',
        reply_markup=keyboard
                        )

if __name__ == '__main__':
    dp.run_polling(bot)