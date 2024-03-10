from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

default_router = Router()


@default_router.message(Command('start'))
async def bot_start(message: Message):
    """Ввод команды /start"""
    await message.answer("Кофе-бот приветствует тебя!")


@default_router.message(Command('name'))
async def command_name(message: Message):
    """Ввод команды /name"""
    await message.answer('Введите свои имя и фамилию')


@default_router.message()
async def get_name(message: Message):
    """Получение имени"""
    name_parts = message.text.strip().split(' ')

    if len(name_parts) != 2 or not all(part.isalpha() for part in name_parts):
        await message.answer('Введите, свои имя и фамилию, состоящие только '
                             'из букв и разделенные пробелом.')
        return

    full_name = ' '.join(part.capitalize() for part in name_parts)
    await message.answer(f'Вас зовут {full_name}')
