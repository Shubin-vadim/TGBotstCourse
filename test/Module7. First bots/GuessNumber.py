from aiogram import F, Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command, Text
import random

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}

ATTEMPTS = 5


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer('Вы вышли из игры. Если захотите играть снова, введите команду /start')
    else:
        await message.answer('Вы не начинали ещё играть. Начните прямо сейчас, введя команду /start!')


@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f"Статистика \n. Всего игры сыграно - {user['total_games']}\n Игры выиграно - {user['wins']}")


@dp.message(Text(text=['Да', 'Давай', 'Я хочу играть!', 'Хочу играть', 'Играть']))
async def process_positive_answer(message: Message):
    if user['in_game']:
        await message.answer('Мы находимся в прицессе игры, я могу только реагировать на число от 1 до 100, а также на команды /cancel и /stat')
    else:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer('Я загадал число от 1 до 100. Попробуй отгадать!')


@dp.message(Text(text=['Нет', 'Нее', 'Я не хочу играть', 'Отстать']))
async def process_negative_answer(message: Message):
    if user['in_game']:
        await message.answer('Мы с тобой сейчас играем, пришли мне число от 1 до 100')
    else:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')


@dp.message(lambda x: x.text and x.text.isdigit() and 1<=int(x.text)<=100)
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            user['in_game'] = True
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Мое число меньше!')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое число больше!')
            user['attempts'] -= 1
        if user['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы ещё не начинали игру. хочешь сыграть?')


@dp.message()
async def process_other_text_message(message: Message):
    if user['in_game']:
        await message.answer('Мы сейчас играем с тобой в игру.\nПрисылай числа от 1 до 100')

    else:
        await message.answer('Я тебя не понимаю, извини((')


def get_random_number() -> int:
    return random.randint(1, 100)


if __name__ == '__main__':
    dp.run_polling(bot)