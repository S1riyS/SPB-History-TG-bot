from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from src.loader import dp
from src.keyboards import get_all_routes
from data import ROUTES


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""

    all_routes_keyboard = get_all_routes()

    description = "Вот наши маршруты:\n"
    for route_id, route_instance in ROUTES.items():
        description += route_instance.short_info + "\n"

    await message.answer(
        # Картинка всего маршрута
        description,
        reply_markup=all_routes_keyboard
    )
