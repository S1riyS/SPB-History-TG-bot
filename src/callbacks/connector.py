from aiogram.types import CallbackQuery

from src.callbacks.factories.connector import ConnectorCallbackFactory
from src.loader import dp


@dp.callback_query(ConnectorCallbackFactory.filter())
async def send_connector_info(callback: CallbackQuery, callback_data: ConnectorCallbackFactory):
    current_route = ROUTES[callback_data.route_id]
    current_checkpoint = current_route.checkpoints[callback_data.checkpoint_index]

    await current_checkpoint.connector.render(callback)
    await callback.answer()
