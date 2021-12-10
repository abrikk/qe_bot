import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils import emoji
from aiogram.utils.markdown import hcode, hitalic

from data.config import CHAT_ID
from keyboards.inline.callback_datas import show_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot
from states import QE


@dp.message_handler(Command("quadratic_equation"))
async def enter_solution(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEM7UFhri8qDycgtpO3xoPl1TAvvv3iTwACWRAAAqFjeUmVY2nNPX10NyIE')
    await message.answer("Напишите через пробел коэффиценты квадратного уравнения ax\u00B2+bx+c=0")

    await QE.E1.set()


@dp.message_handler(state=QE.E1)
async def answer_q1(message: types.Message, state: FSMContext):
    user_text = message.text
    coeff = user_text.split()
    uff_text = f'A message from user {message.from_user.get_mention(as_html=True)}' \
               f'\ntext: "{hitalic(user_text)}"'
    if len(coeff) < 3:
        await message.answer("error. число коэффициентов меньше чем надо")
        await bot.send_message(chat_id=CHAT_ID, text=uff_text)
        await state.reset_state()
    elif len(coeff) > 3:
        await message.answer("error. число коэффициентов больше чем надо")
        await bot.send_message(chat_id=CHAT_ID, text=uff_text)
        await state.reset_state()
    else:
        err_text = f"Ошибка! Вы не правильно ввели коэффициенты.{emoji.emojize(':confused:')}\n\n" \
                   f"Пример того как правильно вводить коэффициенты: \n" \
                   f"x² − 8x + 12 = 0 → \"{hcode('1 -8 12')}\""
        try:
            a = int(coeff[0])
            if a == 0:
                await message.answer("Ошибка! коэффициент a \u2260 0!")
                await state.reset_state()
            else:
                try:
                    a = int(coeff[0])
                    b = int(coeff[1])
                    c = int(coeff[2])
                    await state.update_data(a=a)
                    await state.update_data(b=b)
                    await state.update_data(c=c)
                except ValueError as ex:
                    await bot.send_message(chat_id=569356638, text=f'An error occured: {ex}')
                    await bot.send_message(chat_id=CHAT_ID, text=f'An error occured: '
                                                                 f'{ex}\nA message '
                                                                 f'from user '
                                                                 f'{message.from_user.get_mention(as_html=True)}'
                                                                 f'\ntext: "{hitalic(user_text)}"')
                    await message.answer(f"{err_text}")
                    await state.reset_state()
                # print(a, b, c)
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
                    await message.answer(f'D = {discr} → D &lt 0\n'
                                         f'X\u2209\u211D - Нет корней', reply_markup=choice)
                await state.reset_state(with_data=False)

        except ValueError as ex:
            await bot.send_message(chat_id=CHAT_ID, text=f'An error occured: '
                                                         f'{ex}\nA message '
                                                         f'from user '
                                                         f'{message.from_user.get_mention(as_html=True)}'
                                                         f'\ntext: "{hitalic(user_text)}"')
            await message.answer(f"{err_text}")
            await state.reset_state()


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


