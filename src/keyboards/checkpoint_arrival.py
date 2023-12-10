from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.callbacks.factories.checkpoint import CheckpointCallbackFactory


def get_arrival_keyboard(route_id: int, checkpoint_index: int):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='На месте',
        callback_data=CheckpointCallbackFactory(route_id=route_id, checkpoint_inde=checkpoint_index),
    )
    return builder.as_markup()
