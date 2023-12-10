from aiogram.types import CallbackQuery
from aiogram import F
from random import randint

from src.loader import dp


@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer()
