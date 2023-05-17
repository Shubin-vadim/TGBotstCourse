from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command


API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


async def process_help_command(message: Message):
    await message.reply('Типо помощь')


async def send_photo_echo(message: Message):
    print(message)
    await message.answer_photo(message.photo[0].file_id)


async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)