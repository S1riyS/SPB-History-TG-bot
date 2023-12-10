from aiogram.types import CallbackQuery

from src.libs._renderable import Renderable
from src.libs._typing import CheckpointDetails
from src.libs.checkpoints_connector import CheckpointsConnector
from src.utils.load_from_static import load_photo


class Checkpoint(Renderable):
    def __init__(self, details: CheckpointDetails, connector: CheckpointsConnector):
        self.details = details
        self.connector = connector

    async def render(self, callback: CallbackQuery) -> None:
        photo = load_photo(self.details.photo_path)
        await callback.message.answer_photo(photo)
