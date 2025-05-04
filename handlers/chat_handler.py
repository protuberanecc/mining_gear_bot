import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, Filter
from conf import ADMIN_ID

router = Router()

from locales import translations
from conf import user_langs

ID_PATTERN = re.compile(r"ID пользователя: (\d+)")

async def extract_user_id_from_admin_reply(message: Message) -> int | None:
    if message.reply_to_message and message.reply_to_message.text:
        match = ID_PATTERN.search(message.reply_to_message.text)
        if match:
            return int(match.group(1))
    return None


class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == ADMIN_ID


@router.message(F.text, F.chat.type == "private", F.chat.id != ADMIN_ID)
async def handle_user_message(message: Message):
    username = message.from_user.username or "Без username"
    user_id = message.from_user.id
    language_code = user_langs.get(user_id, "ru")
    user_text = message.text or "<без текста>"

    admin_text = (
        f"Сообщение от пользователя: @{username}\n"
        f"ID пользователя: {user_id}\n\n"
        f"Сообщение:\n{user_text}"
    )

    await message.bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")
    await message.answer(translations["message_to_support_successful"][language_code])



@router.message(F.reply_to_message, F.chat.id == ADMIN_ID)
async def handle_admin_reply(message: Message):
    user_id = await extract_user_id_from_admin_reply(message)
    language_code = user_langs.get(user_id, "ru")

    if not user_id:
        await message.reply("❌ Не удалось извлечь ID пользователя из текста.")
        return

    try:
        await message.bot.send_message(chat_id=user_id, text=f"{translations["support_answer"][language_code]}\n\n{message.text}")
        await message.reply("✅ Ответ отправлен пользователю.")
    except Exception as e:
        await message.reply(f"❌ Ошибка отправки: {e}")
