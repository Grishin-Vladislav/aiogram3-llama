import asyncio
import logging
import sys
import os

from openai import OpenAI
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv, find_dotenv

import message_router

load_dotenv(find_dotenv())


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    await bot.delete_webhook(drop_pending_updates=True)

    client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")
    dp = Dispatcher(client=client)
    dp.include_routers(message_router.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if BOT_TOKEN is None:
        raise ValueError("BOT_TOKEN is not set")

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
