import asyncio
import os

from aiogram import Bot, Dispatcher, types, filters
from handlers.user_private import user_private_router

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)

dp.message(filters.Command('dice'))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__  ==  "__main__":
    asyncio.run(main())