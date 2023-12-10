from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.factories.connector import ConnectorCallbackFactory


def get_next_keyboard(route_id: int, checkpoint_index: int):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Далее',
        callback_data=ConnectorCallbackFactory(route_id=route_id, checkpoint_index=checkpoint_index),
    )
    return builder.as_markup()
