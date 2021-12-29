from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils.markdown import hcode

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Отправьте коэффициенты квадратного уравнения через пробел.\n"
            f"Например: 9x²-6x+1=0 → \"{hcode('9 -6 1')}\""
            "Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/test - Начать тест")
    
    await message.answer("\n".join(text))
