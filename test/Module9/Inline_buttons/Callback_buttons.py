from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.filters import CommandStart, Text

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


cal_btn1: InlineKeyboardButton = InlineKeyboardButton(
    text='КНОПКААА1',
    callback_data='big_button_1_pressed'
)

cal_btn2: InlineKeyboardButton = InlineKeyboardButton(
    text='КНОПКААА2',
    callback_data='big_button_2_pressed'
)

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[cal_btn1],
                     [cal_btn2]]
)

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(Text(text=['big_button_1_pressed']))
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 1', show_alert=True)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(Text(text=['big_button_2_pressed']))
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 2', show_alert=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки',
        reply_markup=keyboard
                        )

if __name__ == '__main__':
    dp.run_polling(bot)