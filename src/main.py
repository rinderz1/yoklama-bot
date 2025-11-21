import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import router


load_dotenv()
# Просто вставь свой токен прямо сюда в кавычки:
TELEGRAM_BOT_TOKEN = "8079601014:AAHI01Rc18KqM4hhs_ux8lRD2CRysxNMx28"

# Проверка (можно оставить)
if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("Токен пустой! Вставь его в код.")


async def main() -> None:
    bot = Bot(
        token=TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
