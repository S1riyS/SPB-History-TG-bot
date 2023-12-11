from aiogram.types import CallbackQuery

from data import ROUTES
from src.factories.route import RouteCallbackFactory
from src.loader import dp


@dp.callback_query(RouteCallbackFactory.filter())
async def send_starting_route_info(
        callback: CallbackQuery, callback_data: RouteCallbackFactory
):
    current_route = ROUTES[callback_data.route_id]
    await current_route.render(callback, callback_data)
    await callback.answer()
