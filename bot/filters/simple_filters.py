from aiogram.filters import BaseFilter
from aiogram.types import Message
from dateparser.search import search_dates
from datetime import datetime


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем список по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False

class DateInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | list[tuple[str, datetime, str]]:
        times: list = search_dates(message.text)
        if times:
            return {'times': times}
        return False


