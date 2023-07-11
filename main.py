import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers import messages, commands
from config import Config, load_config


async def main() -> None:
    # Bot object and dispatcher
    config: Config = load_config('.env')
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(messages.router)
    dp.include_router(commands.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
