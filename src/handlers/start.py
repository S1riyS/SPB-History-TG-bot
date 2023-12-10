from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from src.loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Начать маршрут",
        callback_data="start_route")
    )
    await message.answer(
        # Картинка всего маршрута
        "ИНФОРМАЦИЯ О МАРШРУТЕ!!!",
        reply_markup=builder.as_markup()
    )
