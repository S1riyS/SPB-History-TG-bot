import typing as t

from aiogram.types import CallbackQuery

from src.factories.connector import ConnectorCallbackFactory
from src.factories.route import RouteCallbackFactory
from src.libs.checkpoint import Checkpoint
from src.libs.typing import RouteDetails
from src.utils.load_from_static import load_photo
from ._renderable import Renderable


class Route(Renderable):
    def __init__(self, details: RouteDetails, checkpoints: t.List[Checkpoint]):
        self.details = details
        self.checkpoints = checkpoints
        self.__link_connectors()

    def __link_connectors(self) -> None:
        for checkpoint in self.checkpoints:
            checkpoint.connector.destination_location = checkpoint.details.location

    async def render(
            self, callback: CallbackQuery, data: RouteCallbackFactory = None
    ) -> None:
        await callback.message.answer(self.details.full_description)
        await callback.message.answer("Лови карту маршрута")

        map_photo = load_photo(self.details.map_photo_path)
        await callback.message.answer_photo(map_photo)

        first_checkpoint_connector = self.checkpoints[0].connector
        connector_data = ConnectorCallbackFactory(
            route_id=data.route_id, checkpoint_index=0
        )

        await first_checkpoint_connector.render(callback, connector_data)
