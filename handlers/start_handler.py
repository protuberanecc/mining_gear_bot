from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import os

router = Router()

from keyboards import start_keyboard
from conf import user_langs
from locales import translations


@router.message(Command('start'))
async def start_message(message: Message):

    photo_path = os.path.join(os.path.dirname(__file__), "img", "bot_tg.webp")
    photo = FSInputFile(photo_path)

    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")

    await message.answer_photo(
        photo=photo,
        caption=translations["start_message"][language_code],
        reply_markup=start_keyboard.get_start_keyboard(language_code)
    )


@router.message(F.text.in_([
    translations["menu_buy"]["uk"],
    translations["menu_buy"]["ru"],
    translations["menu_buy"]["en"],
    translations["menu_buy"]["kz"],
]))
async def buy_asic(message: Message):

    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")

    photo_path = os.path.join(os.path.dirname(__file__), "img", "sp.webp")

    photo = FSInputFile(photo_path)

    await message.answer_photo(
        photo=photo,
        caption=translations["message_to_manager"][language_code],
        reply_markup=start_keyboard.get_buy_asic_keyboard(language_code)
    )


@router.message(F.text.in_([
    translations["menu_price"]["uk"],
    translations["menu_price"]["ru"],
    translations["menu_price"]["en"],
    translations["menu_price"]["kz"],
]))
async def buy_asic(message: Message):

    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")

    await message.answer(translations["price_list"][language_code], reply_markup=start_keyboard.get_price_list_keyboard(language_code))


@router.message(F.text.in_([
    translations["menu_site"]["uk"],
    translations["menu_site"]["ru"],
    translations["menu_site"]["en"],
    translations["menu_site"]["kz"],
]))
async def buy_asic(message: Message):

    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")

    await message.answer(translations["our_site"][language_code], reply_markup=start_keyboard.get_open_site_keyboard(language_code))