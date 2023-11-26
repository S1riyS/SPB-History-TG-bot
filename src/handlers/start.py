from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
