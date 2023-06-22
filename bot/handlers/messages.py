from aiogram.types import Message, ContentType
from aiogram import Dispatcher, F


# for photos
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# for audio
async def send_audio_echo(message: Message):
    await message.reply_audio(message.voice.file_id)


# for all messages must be last
async def send_echo(message: Message):
    await message.reply(text=message.text)


# register all handlers
def handlers_messages_register(dp: Dispatcher):
    dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
    dp.message.register(send_audio_echo, F.content_type == ContentType.VOICE)
    dp.message.register(send_echo)
