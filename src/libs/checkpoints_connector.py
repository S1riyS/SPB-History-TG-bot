import typing as t
from pathlib import Path
from random import choice

from aiogram.types import CallbackQuery

from src.factories.connector import ConnectorCallbackFactory
from src.keyboards.checkpoint_arrival import get_arrival_keyboard
from ._renderable import Renderable


class CheckpointsConnector(Renderable):
    """Information of how to get to the current checkpoint"""

    def __init__(
            self, itinerary_comment: str, itinerary_photo_path: t.Optional[Path] = None
    ):
        self.itinerary_comment = itinerary_comment
        self.itinerary_photo_path = itinerary_photo_path
        self.destination_location: t.Optional[str] = None

        self.NEXT_CHECKPOINT_PHRASES = [
            "Держим путь до",
            "Наша следующая остановка",
            "Адрес следующей достопремечательности",
            "Теперь движемся к",
        ]

    def __get_phrase(self) -> str:
        return f"{choice(self.NEXT_CHECKPOINT_PHRASES)}: {self.destination_location}"

    async def render(
            self, callback: CallbackQuery, data: ConnectorCallbackFactory = None
    ) -> None:
        # itinerary_photo = load_photo(self.itinerary_photo_path)
        # await callback.message.answer_photo(itinerary_photo)

        phrase = self.__get_phrase()

        arrival_keyboard = get_arrival_keyboard(data.route_id, data.checkpoint_index)

        await callback.message.answer(
            f"{self.itinerary_comment}\n{phrase}", reply_markup=arrival_keyboard
        )
