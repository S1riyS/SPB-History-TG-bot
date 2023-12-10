from aiogram.filters.callback_data import CallbackData


class RouteCallbackFactory(CallbackData, prefix="start_route"):
    route_id: int
