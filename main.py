import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers import messages, commands
from config import Config, load_config


async def main() -> None:
    # Bot object and dispatcher
    config: Config = load_config('.env')
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    #это надо утащить в стартовый сетап
    messages.setup(dp=dp)
    commands.setup(dp=dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
