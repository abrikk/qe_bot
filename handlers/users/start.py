import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils import emoji
from aiogram.utils.markdown import hbold, hcode, hitalic

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            user_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(user_id=message.from_user.id)
    await message.answer_sticker('CAACAgIAAxkBAAEM6NlhrN1WqOOf97mQRgUyx0_4IQ2bYwACZREAAmGVgUkjYSlO6WhLgiIE')
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!{emoji.emojize(':wave:')}\n\n"
                         f"Чтобы решить квадратное уравнение отправьте его "
                         f"коэффициенты через {hbold('пробел')}\n\n"
                         f"Например: x² + 4x + 3 = 0 → \"{hcode('1 4 3')}\"\n\n"
                         f"Посмотреть статистику бота - {hitalic('/statistics')}")
