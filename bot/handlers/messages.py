from aiogram.types import Message, ContentType
from aiogram import Dispatcher, F
from bot.filters.simple_filters import NumbersInMessage

# for photos
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# for audio
async def send_voice_echo(message: Message):
    await message.reply_audio(message.voice.file_id)


# for Video
async def send_video_echo(message: Message):
    await message.reply_audio(message.video.file_id)


# for Sticker
async def send_document_echo(message: Message):
    await message.reply_audio(message.document.file_id)


async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')

# for all messages must be last
async def send_echo(message: Message):
    await message.reply(text=message.text)



# register all handlers
def handlers_messages_register(dp: Dispatcher):
    dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
    dp.message.register(send_voice_echo, F.content_type == ContentType.VOICE)
    dp.message.register(send_video_echo, F.content_type == ContentType.VIDEO)
    dp.message.register(send_document_echo, F.content_type == ContentType.DOCUMENT)
    dp.message.register(process_if_numbers, F.Text(startwith='найди числа', ignore_case=True))
    dp.message.register(send_echo)
