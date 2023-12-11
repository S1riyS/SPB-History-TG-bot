from aiogram.types import CallbackQuery

from data import ROUTES
from src.factories.checkpoint import CheckpointCallbackFactory
from src.loader import dp


@dp.callback_query(CheckpointCallbackFactory.filter())
async def send_checkpoint_info(callback: CallbackQuery, callback_data: CheckpointCallbackFactory):
    # Retrieving checkpoint object
    current_route = ROUTES[callback_data.route_id]
    current_checkpoint = current_route.checkpoints[callback_data.checkpoint_index]
    # Sending information about chechpoint to user
    await current_checkpoint.render(callback, callback_data)
    await callback.answer()
