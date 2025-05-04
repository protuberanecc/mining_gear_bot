from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from locales import translations


def get_start_keyboard(lang: str = "ru") -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=translations["menu_buy"][lang])],
                [KeyboardButton(text=translations["menu_price"][lang])],
                [KeyboardButton(text=translations["menu_site"][lang])],
                [KeyboardButton(text=translations["menu_language"][lang])]
            ],
            resize_keyboard=True,
            input_field_placeholder=translations["menu_placeholder"][lang]
        )


def get_open_site_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=translations["open_site"][lang], web_app=WebAppInfo(url='https://mining-gear-ua.com/catalog'))]
            ]
        )


def get_buy_asic_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=translations["buy_asic"][lang], url='https://t.me/ALEXmininggear')]
            ]
        )


def get_price_list_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=translations["open_price_list"][lang], url='https://docs.google.com/spreadsheets/d/1wUFG3i-BgVAqF_mRbZRX7c2DUIBA543DndVWsOgOAMQ/')]
            ]
        )


language_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🇺🇦 UK 🇺🇦', callback_data='uk')],
        [InlineKeyboardButton(text='🇷🇺 RU 🇷🇺', callback_data='ru')],
        [InlineKeyboardButton(text='🇺🇸 EN 🇺🇸', callback_data='en')],
        [InlineKeyboardButton(text='🇰🇿 KZ 🇰🇿', callback_data='kz')],
    ]
)