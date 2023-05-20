from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

API_TOKEN = '6277553592:AAGJCdQI7TtN3iNBB45kSPMPARlFuOXKd8U'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка о боте'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Контакты'),
        BotCommand(command='/pay',
                   description='Платежи'),
    ]
    await bot.set_my_commands(main_menu_commands)

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)