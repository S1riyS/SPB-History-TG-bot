from aiogram.filters.callback_data import CallbackData


class ConnectorCallbackFactory(CallbackData, prefix="goto"):
    route_id: int
    checkpoint_index: int
