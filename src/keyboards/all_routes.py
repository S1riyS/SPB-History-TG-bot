from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import ROUTES
from src.factories.route import RouteCallbackFactory


def get_all_routes():
    builder = InlineKeyboardBuilder()
    for route_id, route_instance in ROUTES.items():
        builder.button(
            text=route_instance.details.name,
            callback_data=RouteCallbackFactory(route_id=route_id),
        )
    builder.adjust(1)
    return builder.as_markup()
