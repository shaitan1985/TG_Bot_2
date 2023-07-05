from aiogram.types import Message, ContentType
from aiogram import Router, F
from aiogram.filters import Text
from bot.filters.simple_filters import NumbersInMessage, DateInMessage
from datetime import datetime

router: Router = Router()


# for photos
@router.message(F.content_type == ContentType.PHOTO)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# for audio
@router.message(F.content_type.in_({ContentType.AUDIO, ContentType.VOICE}))
async def send_voice_echo(message: Message):
    await message.reply_audio(message.voice.file_id)


# for Video
@router.message(F.content_type == ContentType.VIDEO)
async def send_video_echo(message: Message):
    await message.reply_audio(message.video.file_id)


@router.message(Text(startswith='найди числа', ignore_case=True), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


@router.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')


@router.message(Text(startswith='найди даты', ignore_case=True), DateInMessage())
async def process_if_dates(message: Message, times: list[tuple[str, datetime, str]]):
    await message.answer(
            text=f'Нашел: {"/n".join(str(line[1]) for line in times)}')


@router.message(Text(startswith='найди даты', ignore_case=True))
async def process_if_not_dates(message: Message):
    await message.answer(
            text='Не нашел дат :(')


# for all messages must be last
@router.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)