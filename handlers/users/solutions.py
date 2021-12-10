from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import show_callback
from loader import dp
from states import QE


@dp.callback_query_handler(show_callback.filter(solution="solve"), state=QE.SM)
async def show_solution(call, state: FSMContext):
    data = await state.get_data()
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    discr = data.get("discr")
    await call.answer(cache_time=60)
    answer_m = f"a = {a}, b = {b}, c = {c}\n" \
               f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n" \
               f"X\u2081 = (-b + \u221AD) / (2 * a) = ({-b} + " \
               f"\u221A{discr}) / (2 * {a})\n" \
               f"X\u2082 = (-b - \u221AD) / (2 * a) = ({-b} - " \
               f"\u221A{discr}) / (2 * {a})"
    await call.message.answer(f'{answer_m}')


@dp.callback_query_handler(show_callback.filter(solution="solve"), state=QE.SE)
async def show_solution(call, state: FSMContext):
    data = await state.get_data()
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    discr = data.get("discr")
    await call.answer(cache_time=60)
    answer_e = f"a = {a}, b = {b}, c = {c}\n" \
               f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n" \
               f"X = -b / (2 * a) = {-b} / (2 * {a})"
    await call.message.answer(f'{answer_e}')


@dp.callback_query_handler(show_callback.filter(solution="solve"), state=QE.SL)
async def show_solution(call, state: FSMContext):
    data = await state.get_data()
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    discr = data.get("discr")
    await call.answer(cache_time=60)
    answer_l = f"a = {a}, b = {b}, c = {c}\n" \
               f"D = b\u00B2-4*a*c = {b}\u00B2-4*{a}*{c}={discr}\n"
    await call.message.answer(f'{answer_l}')
