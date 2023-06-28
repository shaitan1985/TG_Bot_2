from aiogram import Bot, Dispatcher
from aiogram.types import Message
from bot.handlers import messages, commands
import config


# Bot object and dispatcher
bot: Bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp: Dispatcher = Dispatcher()


if __name__ == '__main__':
    messages.setup(dp=dp)
    commands.setup(dp=dp)
    dp.run_polling(bot)
