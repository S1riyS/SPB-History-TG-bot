from aiogram.types import CallbackQuery

from src.keyboards.checkpoint_next import get_next_keyboard
from src.libs.checkpoints_connector import CheckpointsConnector
from src.libs.typing import CheckpointDetails
from ._renderable import Renderable


class Checkpoint(Renderable):
    def __init__(self, details: CheckpointDetails, connector: CheckpointsConnector):
        self.details = details
        self.connector = connector

    async def render(self, callback: CallbackQuery, *args, **kwargs):
        """
        :param callback: Callback object
        :keyword CheckpointCallbackFactory data: Callback data
        :return: None, as it sends messages via passed callback
        """
        callback_data = kwargs.get('data')

        # photo = load_photo(self.details.photo_path)
        # await callback.message.answer_photo(photo)

        next_checkpoint_index = callback_data.checkpoint_index + 1
        next_keyboard = get_next_keyboard(callback_data.route_id, next_checkpoint_index)
        await callback.message.answer(self.details.description, reply_markup=next_keyboard)
