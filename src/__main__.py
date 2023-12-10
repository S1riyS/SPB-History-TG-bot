import asyncio
import logging
import sys
import src.handlers
import src.callbacks

from src.loader import bot
from src.loader import dp


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
