from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils import emoji
from aiogram.utils.markdown import hbold

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEM6NlhrN1WqOOf97mQRgUyx0_4IQ2bYwACZREAAmGVgUkjYSlO6WhLgiIE')
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!{emoji.emojize(':wave:')}\n\n"
                         f"Решить квадратное уравнение - /quadratic_equation")
