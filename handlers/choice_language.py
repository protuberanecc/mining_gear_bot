from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from keyboards import start_keyboard
from locales import translations, LANGUAGES
from conf import user_langs

router = Router()


@router.message(F.text.in_([
    translations["menu_language"]["uk"],
    translations["menu_language"]["ru"],
    translations["menu_language"]["en"],
    translations["menu_language"]["kz"],
]))
async def choose_language(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[]
    )

    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")

    for code, name in LANGUAGES.items():
        keyboard.inline_keyboard.append(
                [InlineKeyboardButton(text=name, callback_data=f"set_language:{code}")],
        )

    await message.answer(translations["choose_lang"][language_code], reply_markup=keyboard)


@router.callback_query(F.data.startswith("set_language:"))
async def callback_set_language(callback: CallbackQuery):
    language_code = callback.data.split(":")[1]
    user_id = callback.from_user.id

    user_langs[user_id] = language_code

    await callback.answer()
    await callback.message.answer(translations["changed_language"][language_code], reply_markup=start_keyboard.get_start_keyboard(language_code))
