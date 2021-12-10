from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/test - Начать тест",
            "/quadratic_equation - Решить квадратное уравнение")
    
    await message.answer("\n".join(text))
