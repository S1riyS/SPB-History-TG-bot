from aiogram.types import CallbackQuery
from aiogram import F
from random import randint

from src.loader import dp


@dp.callback_query(F.data == "start_route")
async def send_random_value(callback: CallbackQuery):
    # await callback.message.answer(// ЗАПУСТИТЬ МАРШРУТ //)
    await callback.answer()
