from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Dispatcher


# handler for start command
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name Echo-bot!\nWrite something')


# handler for help command
async def process_help_command(message: Message):
    await message.answer('You can write somthing? and i will send it back')


# register all handlers
def handlers_commands_register(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands=["start"]))
    dp.message.register(process_help_command, Command(commands=["help"]))
