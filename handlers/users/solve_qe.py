import math

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.utils import emoji
from aiogram.utils.markdown import hitalic, hcode

from data.config import CHAT_ID
from keyboards.inline.callback_datas import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot

qe_regexp = r'-?[\d+]{1,15}\s+-?[\d+]{1,15}\s+-?[\d+]{1,15}$'


@dp.message_handler(filters.Regexp(qe_regexp))
async def regexp_example(message: types.Message, state: FSMContext):
    user_text = message.text
    await bot.send_message(chat_id=CHAT_ID, text=f"{hcode('SOLVE_QE')}\n"
                                                 f"Сообщения от пользователя "
                                                 f"{message.from_user.get_mention()}:"
                                                 f" {user_text}")
    coeff = user_text.split()
    err_text = f"Ошибка! Вы не правильно ввели коэффициенты.{emoji.emojize(':confused:')}\n\n" \
               f"Пример того как правильно вводить коэффициенты: \n" \
               f"x² − 8x + 12 = 0 → \"{hcode('1 -8 12')}\""

    a = int(coeff[0])
    if a == 0:
        await message.answer("Ошибка! коэффициент a \u2260 0!")
        await state.reset_state()
    else:
        a = int(coeff[0])
        b = int(coeff[1])
        c = int(coeff[2])
        await state.update_data(a=a)
        await state.update_data(b=b)
        await state.update_data(c=c)

        discr = pow(b, 2) - 4 * a * c
        await state.update_data(discr=discr)
        # настройка коэфф. b
        if not str(b).startswith("-") and b != 1:
            b_str = f"+{b}x"
        elif not str(b).startswith("-") and b == 1:
            b_str = "+x"
            print(b_str)
        elif b != -1:
            b_str = f"{b}x"
        else:
            b_str = "-x"
        # настройка коэфф. c
        if not str(c).startswith("-"):
            c_str = f"+{c}"
        else:
            c_str = c
        if b == 0:
            if c == 0 and a == 1:
                await message.answer(f"Коэффиценты неполного квадратного уравнения x\u00B2=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif c != 0 and a == 1:
                await message.answer(f"Коэффиценты неполного приведенного квадратного уравнения "
                                     f"x\u00B2{c_str}=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif c == 0 and a == -1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"-x\u00B2=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif c != 0 and a == -1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"-x\u00B2{c_str}=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif c != 0 and a != 1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного "
                                     f"уравнения {a}x\u00B2{c_str}=0:\n "
                                     f"a = {a}, b = {b}, c = {c}")
            elif c == 0 and a != 1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"{a}x\u00B2=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")

        elif c == 0:
            if b != 0 and a == 1:
                await message.answer(f"Коэффиценты неполного приведенного квадратного уравнения "
                                     f"x\u00B2{b_str}=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif b == 0 and a == -1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"-x\u00B2=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif b != 0 and a == -1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"-x\u00B2{b_str}=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")
            elif b != 0 and a != 1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного "
                                     f"уравнения {a}x\u00B2{b_str}=0:\n "
                                     f"a = {a}, b = {b}, c = {c}")
            elif b == 0 and a != 1:
                await message.answer(f"Коэффиценты неполного неприведенного квадратного уравнения "
                                     f"{a}x\u00B2=0:\n"
                                     f"a = {a}, b = {b}, c = {c}")

        elif a == 1:
            await message.answer(f"Коэффиценты приведенного квадратного уравнения "
                                 f"x\u00B2{b_str}{c_str}=0:\n"
                                 f"a = {a}, b = {b}, c = {c}")
        elif a == -1:
            await message.answer(f"Коэффиценты приведенного квадратного уравнения "
                                 f"-x\u00B2{b_str}{c_str}=0:\n"
                                 f"a = {a}, b = {b}, c = {c}")
        else:
            await message.answer(f"Коэффиценты уравнения {a}x\u00B2{b_str}{c_str}=0:\n"
                                 f"a = {a}, b = {b}, c = {c}")

        if discr > 0:
            x1 = round((-b + math.sqrt(discr)) / (2 * a), 3)
            x2 = round((-b - math.sqrt(discr)) / (2 * a), 3)
            await message.answer(f'D = {discr}\n'
                                 f'X\u2081 = {x1}, '
                                 f'X\u2082 = {x2}', reply_markup=choice)

        elif discr == 0:
            x = round(-b / (2 * a), 3)
            await message.answer(f'D = {discr}\n'
                                 f'X = {x}', reply_markup=choice)

        elif discr < 0:
            await message.answer(f'D = {discr}, нет корней\n'
                                 f'Так как D &lt 0 → X\u2209\u211D ', reply_markup=choice)
        await state.reset_state(with_data=False)


@dp.callback_query_handler(show_callback.filter(solution="solve"))
async def show_solution(call, state: FSMContext):
    data = await state.get_data()
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    discr = data.get("discr")
    if discr > 0:
        await call.answer(cache_time=60)
        answer_m = f"a = {a}, b = {b}, c = {c}\n" \
                   f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n" \
                   f"X\u2081 = (-b + \u221AD) / (2 * a) = ({-b} + " \
                   f"\u221A{discr}) / (2 * {a})\n" \
                   f"X\u2082 = (-b - \u221AD) / (2 * a) = ({-b} - " \
                   f"\u221A{discr}) / (2 * {a})"
        await call.message.answer(f'{answer_m}')
    elif discr == 0:
        await call.answer(cache_time=60)
        answer_e = f"a = {a}, b = {b}, c = {c}\n" \
                   f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n" \
                   f"X = -b / (2 * a) = {-b} / (2 * {a})"
        await call.message.answer(f'{answer_e}')
    elif discr < 0:
        await call.answer(cache_time=60)
        answer_l = f"a = {a}, b = {b}, c = {c}\n" \
                   f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n"
        await call.message.answer(f'{answer_l}')
