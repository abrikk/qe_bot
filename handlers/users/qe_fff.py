import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils import emoji
from aiogram.utils.markdown import hcode

from keyboards.inline.callback_datas import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot
from states import QE


@dp.message_handler(Command("qeee"))
async def enter_solution(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEM7UFhri8qDycgtpO3xoPl1TAvvv3iTwACWRAAAqFjeUmVY2nNPX10NyIE')
    await message.answer("Напишите через пробел коэффиценты квадратного уравнения ax\u00B2+bx+c=0")

    await QE.E1.set()


@dp.message_handler(state=QE.E1)
async def answer_q1(message: types.Message, state: FSMContext):
    global a, b, c
    coeff = message.text.split()
    if len(coeff) < 3 or len(coeff) > 3:
        await state.reset_state()
    if int(coeff[0]) == 0:
        raise ValueError("Coefficient 'a' cannot be equal to zero")
    try:
        a!=0
    except ValueError as ex:
        await message.answer("Ошибка! коэффициент a \u2260 0!")
        await state.reset_state()
    try:
        a = int(coeff[0])
        b = int(coeff[1])
        c = int(coeff[2])
    except ValueError as ex:
        await bot.send_message(chat_id=569356638, text=f'an error occured: {ex}')
        await message.answer(f"Ошибка! Вы не правильно ввели коэффициенты.{emoji.emojize(':confused:')}\n\n"
                             f"Пример того как правильно вводить коэффициенты: \n"
                             f"x² − 8x + 12 = 0 → \"{hcode('1 -8 12')}\"")
        await state.reset_state()
    # except ZeroDivisionError as ex:
    #     await bot.send_message(chat_id=569356638, text=f'an error occured: {ex}')
    #     await message.answer("Ошибка! коэффициент a \u2260 0!")
    #     await state.reset_state()
    if a == 0:
        await message.answer("Ошибка! Коэффициент a \u2260 0!")
        await state.reset_state()

    # await state.update_data(a=a)
    # await state.update_data(b=b)
    # await state.update_data(c=c)

    await QE.Con.set()
    if not str(b).startswith("-"):
        b_str = f"+{b}"
    else:
        b_str = b
    if not str(c).startswith("-"):
        c_str = f"+{c}"
    else:
        c_str = c
    if a == 1:
        await message.answer(f"Коэффиценты уравнения x\u00B2{b_str}x{c_str}=0:\n"
                             f"a = {a}, b = {b}, c = {c}")
    elif a == -1:
        await message.answer(f"Коэффиценты уравнения -x\u00B2{b_str}x{c_str}=0:\n"
                             f"a = {a}, b = {b}, c = {c}")
    else:
        await message.answer(f"Коэффиценты уравнения {a}x\u00B2{b_str}x{c_str}=0:\n"
                             f"a = {a}, b = {b}, c = {c}")

    discr = pow(b, 2) - 4 * a * c
    # data = await state.get_data()
    # a = data.get("a")
    # b = data.get("b")
    # c = data.get("c")
    if discr > 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 3)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 3)
        await message.answer(f'D = {discr}\n'
                             f'X\u2081 = {x1}, '
                             f'X\u2082 = {x2}', reply_markup=choice)

        @dp.callback_query_handler(show_callback.filter(solution="solve"))
        async def show_solution(call: CallbackQuery):
            await call.answer(cache_time=60)
            await call.message.answer(f"a = {a}, b = {b}, c = {c}\n"
                                      f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n"
                                      f"X\u2081 = (-b + \u221AD) / (2 * a) = ({-b} + \u221A{discr}) / (2 * {a})\n"
                                      f"X\u2082 = (-b - \u221AD) / (2 * a) = ({-b} - \u221A{discr}) / (2 * {a})")
    elif discr == 0:
        x = round(-b / (2 * a), 3)
        await message.answer(f'D = {discr}\n'
                             f'X = {x}', reply_markup=choice)

        @dp.callback_query_handler(show_callback.filter(solution="solve"))
        async def show_solution(call: CallbackQuery):
            await call.answer(cache_time=60)
            await call.message.answer(f"a = {a}, b = {b}, c = {c}\n"
                                      f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n"
                                      f"X = -b / (2 * a) = {-b} / (2 * {a})")
    elif discr < 0:
        await message.answer(f'D = {discr} → D &lt 0\n'
                             f'X\u2209\u211D - Нет корней', reply_markup=choice)

        @dp.callback_query_handler(show_callback.filter(solution="solve"))
        async def show_solution(call: CallbackQuery):
            await call.answer(cache_time=60)
            await call.message.answer(f"a = {a}, b = {b}, c = {c}\n"
                                      f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n")

    else:
        await message.answer('Ошибка!')
    await state.reset_state()
