import typing as t
from abc import ABC
from abc import abstractmethod

from aiogram.types import CallbackQuery


class Renderable(ABC):
    @abstractmethod
    async def render(self, callback: CallbackQuery, data: t.Any = None) -> None:
        ...
