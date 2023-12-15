import asyncio
import logging
import sys

from src.config import START_POLLING
from src.loader import bot
from src.loader import dp


async def main() -> None:
    from src import handlers
    from src import callbacks

    if START_POLLING:
        await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
