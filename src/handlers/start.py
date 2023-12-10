from aiogram.filters import CommandStart
from aiogram.types import Message

from data import ROUTES
from src.keyboards.all_routes import get_all_routes
from src.loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""

    all_routes_keyboard = get_all_routes()

    description = "Вот наши маршруты:\n"
    for route_id, route_instance in ROUTES.items():
        description += route_instance.details.brief_description + "\n"

    await message.answer(description, reply_markup=all_routes_keyboard)
