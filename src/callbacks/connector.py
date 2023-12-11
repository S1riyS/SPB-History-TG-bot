from aiogram.types import CallbackQuery

from data import ROUTES
from src.factories.connector import ConnectorCallbackFactory
from src.keyboards.all_routes import get_all_routes
from src.loader import dp


@dp.callback_query(ConnectorCallbackFactory.filter())
async def send_connector_info(callback: CallbackQuery, callback_data: ConnectorCallbackFactory):
    current_route = ROUTES[callback_data.route_id]

    # Checking if checkpoint_index is in range
    if len(current_route.checkpoints) > callback_data.checkpoint_index:
        current_checkpoint = current_route.checkpoints[callback_data.checkpoint_index]
        await current_checkpoint.connector.render(callback, data=callback_data)
    # Sending message that route is finished
    else:
        all_routes_keyboard = get_all_routes()
        await callback.message.answer(
            "Маршрут окончен.\nВы можете так же попробовать:",
            reply_markup=all_routes_keyboard,
        )

    await callback.answer()
