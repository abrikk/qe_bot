from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import emoji
from aiogram.utils.markdown import hcode, hbold, hunderline

from data.config import CHAT_ID
from loader import dp, bot
from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование \n"
                         "Вопрос №1. \n\n"
                         "Что общего у чайника и парохода?")

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    answer = answer.lower()
    if answer == "пар":
        await message.answer("Верный ответ!")

    await message.answer("Вопрос №2 \n\n"
                         "Что общего у гоночного болида и торнадо?")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text
    await state.update_data(answer2=answer2)
    answer2 = answer2.lower()
    if answer2 == "вращение":
        await message.answer("Верный ответ!")

    await message.answer("Вопрос №3 \n\n"
                         "Что общего у ботинка и карандаша?")
    await Test.Q3.set()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text
    await state.update_data(answer3=answer3)
    answer3_c = answer3.lower()
    if answer3_c == "след":
        await message.answer("Верный ответ!")

    await bot.send_message(chat_id=CHAT_ID, text=f"Ответы на тест от пользователя "
                                                        f"{message.from_user.get_mention(as_html=True)}:\n\n"
                                                        f"Ответ 1: {hunderline(answer1)}\n"
                                                        f"Ответ 2: {hunderline(answer2)}\n"
                                                        f"Ответ 3: {hunderline(answer3)}")
    await message.answer(f"Всё ясно... \nУ Вас Шизофрения...{emoji.emojize(':grin:')}\n"
                         "Вот Ваши ответы:\n"
                         f"Ответ 1: {hcode(answer1)}\n"
                         f"Ответ 2: {hcode(answer2)}\n"
                         f"Ответ 3: {hcode(answer3)}")

    await message.answer("Внимание, а теперь правильные ответы:\n"
                         f"1 - {hbold('Пар')} (пароход двигается благодаря пару, а чайник выпускает пар "
                         f"закипая).\n"
                         f"2 - {hbold('Вращение')} (торнадо вращается вокруг своей оси и колеса болида "
                         f"вращаются вокруг своей "
                         "оси).\n "
                         f"3 - {hbold('Оба оставляют следы')} (карандаш при рисовании и ботинок при ходьбе).")

    await state.reset_state()
