from aiogram import Bot, Dispatcher
from aiogram.types import Message

import config
from bot.handlers import commands, messages
# Bot object and dispatcher
bot: Bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp: Dispatcher = Dispatcher()


if __name__ == '__main__':
    commands.handlers_commands_register(dp=dp)
    messages.handlers_messages_register(dp=dp)
    dp.run_polling(bot)
