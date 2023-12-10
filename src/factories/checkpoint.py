from aiogram.filters.callback_data import CallbackData


class CheckpointCallbackFactory(CallbackData, prefix="checkpoint"):
    route_id: int
    checkpoint_index: int
