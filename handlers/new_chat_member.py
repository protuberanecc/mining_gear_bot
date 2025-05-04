from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType

router = Router()

last_welcome_messages: dict[int, int] = {}

@router.message(F.new_chat_members, F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def handle_new_members(message: Message):
    chat_id = message.chat.id

    try:
        await message.delete()
    except Exception as e:
        print(f"[!] Не удалось удалить системное сообщение: {e}")

    last_message_id = last_welcome_messages.get(chat_id)
    if last_message_id:
        try:
            await message.bot.delete_message(chat_id=chat_id, message_id=last_message_id)
        except Exception as e:
            print(f"[!] Не удалось удалить предыдущее приветствие: {e}")

    names = [user.full_name for user in message.new_chat_members]
    welcome_text = (
        f"{message.from_user.first_name or ''} {message.from_user.last_name or ''} — Добро пожаловать в чат <b><a href='https://t.me/mininggearUA'>MiningGear</a></b>!"
        f"\n\n💡 Доступные цены"
        f"\n💡 Доставка до двери"
        f"\n💡 Консультации по покупке"
        f"\n💡 Помощь с хостингом"
        f"\n\nЛюбая реклама запрещена = БАН"
        f"\n\nДля покупки оборудования:"
        f"\n<a href='https://t.me/ALEXmininggear'>* @ALEXmininggear</a>"
        f"\n<a href='https://t.me/SERGEYmininggear'>* @SERGEYmininggear</a>"
        f"\n\nТех вопросы:"
        f"\n<a href='https://t.me/maninggearHELP'>* @maninggearHELP</a>"
        f"\n\nПодпишитесь на канал ➡️ <a href='https://t.me/mininggearUA'>MiningGear</a> чтобы быть в курсе новостей"
    )

    try:
        sent_message = await message.answer(welcome_text, parse_mode="HTML", disable_web_page_preview=True)
        last_welcome_messages[chat_id] = sent_message.message_id
    except Exception as e:
        print(f"[!] Не удалось отправить приветствие: {e}")