from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Dispatcher


#start filter for example
def start_filter(message: Message) -> bool:
    return message.text == '/start'


# handler for start command
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name Echo-bot!\nWrite something')


# handler for help command
async def process_help_command(message: Message):
    await message.answer('You can write somthing? and i will send it back')


# register all handlers
def setup(dp: Dispatcher):
    dp.message.register(process_start_command, start_filter)
    dp.message.register(process_help_command, Command(commands=["help"]))
