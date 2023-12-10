from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import ROUTES
from src.callbacks.factories.start_route import RouteCallbackFactory


def get_all_routes():
    builder = InlineKeyboardBuilder()
    for route_id, route_instance in ROUTES.items():
        builder.button(
            text=route_instance.name, callback_data=RouteCallbackFactory(route_id=route_id)
        )
    builder.adjust(1)
    return builder.as_markup()
