import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(find_dotenv())

memory_storage = MemoryStorage()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=memory_storage)

DATABASE_URL = os.getenv('DATABASE')