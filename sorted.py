from aiogram.dispatcher import Dispatcher
from aiogram.bot import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storages = MemoryStorage()


bot = Bot(token='MY_TOKEN')
dp = Dispatcher(bot, storage=storages)
