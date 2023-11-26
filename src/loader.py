from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode

from src.config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
