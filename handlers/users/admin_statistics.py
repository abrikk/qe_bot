from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("statistics"))
async def bot_start(message: types.Message):
    user = await db.select_user(user_id=message.from_user.id)
    access = user.get('access')
    count_users = await db.count_users()

    if access == 0:
        await message.answer(f"Всего пользователей в боте: {count_users}")
    else:
        await message.answer_sticker('CAACAgIAAxkBAAEM6OFhrN9vdQi7VP6Z3gUWSraCzsjQwQACLxEAArFFgUmaJjI1dNW5xyIE')
