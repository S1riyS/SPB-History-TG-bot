from aiogram.types import CallbackQuery

from src.factories.checkpoint import CheckpointCallbackFactory
from src.keyboards.checkpoint_next import get_next_keyboard
from src.libs.checkpoints_connector import CheckpointsConnector
from src.libs.typing import CheckpointDetails
from ._renderable import Renderable


class Checkpoint(Renderable):
    def __init__(self, details: CheckpointDetails, connector: CheckpointsConnector):
        self.details = details
        self.connector = connector

    async def render(
            self, callback: CallbackQuery, data: CheckpointCallbackFactory = None
    ) -> None:
        # photo = load_photo(self.details.photo_path)
        # await callback.message.answer_photo(photo)

        next_keyboard = get_next_keyboard(data.route_id, data.checkpoint_index + 1)
        await callback.message.answer(
            self.details.description, reply_markup=next_keyboard
        )
