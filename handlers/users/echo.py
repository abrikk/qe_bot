from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import emoji

from data.config import CHAT_ID
from loader import dp, bot


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEM6OFhrN9vdQi7VP6Z3gUWSraCzsjQwQACLxEAArFFgUmaJjI1dNW5xyIE')
    misunder = f"Упс...{emoji.emojize(':face_with_hand_over_mouth:')}\n" \
               f"Вы ввели что-то не понятное\nЧтобы узнать доступные " \
               f"команды отправьте /help {emoji.emojize(':backhand_index_pointing_left:')}"
    await message.answer(f"{misunder}")
    text = f"Сообщение от пользователя " \
           f"{message.from_user.get_mention(as_html=True)} : {message.text}"
    await bot.send_message(chat_id=CHAT_ID, text=text)


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer_sticker('CAACAgIAAxkBAAEM6OFhrN9vdQi7VP6Z3gUWSraCzsjQwQACLxEAArFFgUmaJjI1dNW5xyIE')
    misunder = f"Упс...{emoji.emojize(':face_with_hand_over_mouth:')}\n" \
               f"Вы ввели что-то не понятное\nЧтобы узнать доступные " \
               f"команды отправьте /help {emoji.emojize(':backhand_index_pointing_left:')}\n" \
               f"Вы в состоянии <code>{state}</code>.\n" \
               f"Вы отправили: {message.content_type}\n"
    await message.answer(f"{misunder}")
    receivedd = message.text
    if receivedd != message.content_type:
        receivedd = message.content_type
    text = f"Сообщение от пользователя " \
           f"{message.from_user.get_mention(as_html=True)} : {receivedd}"
    await bot.send_message(chat_id=CHAT_ID, text=text)
