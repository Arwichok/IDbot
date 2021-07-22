import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.utils.settings import Settings
from app import handlers


async def polling(dp: Dispatcher):
    try:
        await dp.start_polling()
    finally:
        await dp.bot.session.close()


def run():
    settings = Settings()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(settings.bot_token, parse_mode="HTML")
    dp = Dispatcher(bot)
    handlers.register(dp)

    try:
        asyncio.run(polling(dp))
    except (KeyboardInterrupt, SystemExit):
        pass
