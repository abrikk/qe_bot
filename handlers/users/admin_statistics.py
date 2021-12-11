import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils import emoji
from aiogram.utils.markdown import hbold

from loader import dp, db


@dp.message_handler(Command("statistics"))
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            user_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(user_id=message.from_user.id)

    access = user.get('access')
    count_users = await db.count_users()

    if access == 777:
        await message.answer(f"Информация для админа:\n"
                             f"Пользователей в боте {count_users}")
    else:
        await message.answer_sticker("CAACAgIAAxkBAAENAAHEYbSUNSxo--kfchVOOEHMYGKDMeoAAi8RAAKxRYFJmiYyNXTVuccjBA")