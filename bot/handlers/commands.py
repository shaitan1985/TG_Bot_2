from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

# Инициализируем роутер уровня модуля
router: Router = Router()


# start filter for example
def start_filter(message: Message) -> bool:
    return message.text == '/start'


# handler for start command
@router.message(start_filter)
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name Echo-bot!\nWrite something')


# handler for help command
@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('You can write somthing? and i will send it back')