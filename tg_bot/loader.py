from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, Redis

from tg_bot.config import BOT_TOKEN, DEBUG


def include_all_routers():
    """ Добавление роутеров. """
    from tg_bot.handlers import all_routers
    dp.include_routers(*all_routers)


bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

if DEBUG:
    storage = MemoryStorage()
else:
    storage = RedisStorage(Redis())

dp = Dispatcher()
include_all_routers()
