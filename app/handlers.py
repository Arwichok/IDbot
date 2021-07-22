import logging

from aiogram import Dispatcher
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent


async def start_c(m: Message):
    await m.answer("I show your id by /id")
    logging.info(f"Start from user {m.from_user.first_name}({m.from_user.id})")


def sticker_text(m: Message):
    return f"\n\nSticker: <code>{m.sticker.file_id}</code>" if m.sticker else ""


async def forward(m: Message):
    chat = m.forward_from if m.forward_from else m.forward_from_chat
    await m.answer(f"Forward from <code>{chat.id}</code>" + sticker_text(m))
    logging.info(f"Forwarded message for {m.from_user.id}")


async def user_id(m: Message):
    await m.answer(f"Your ID: <code>{m.from_user.id}</code>" + sticker_text(m))
    logging.info(f"User id: {m.from_user.id}")


async def chat_id(m: Message):
    await m.answer(
        f"Your ID: <code>{m.from_user.id}</code>\n"
        f"Chat ID: <code>{m.chat.id}</code>")
    logging.info(f"ID chat: {m.chat.id} from {m.chat.id}")


async def inline(iq: InlineQuery):
    result = InlineQueryResultArticle(
        id="_",
        title=f"Your ID: {iq.from_user.id}",
        description="Tap to send your ID to chat",
        input_message_content=InputTextMessageContent(
            message_text=f"My Telegram ID: <code>{iq.from_user.id}</code>"
        )
    )
    await iq.answer([result], cache_time=300, is_personal=True)
    logging.info(f"Inline from {iq.from_user.id}")


def register(dp: Dispatcher):
    dp.register_message_handler(start_c, commands="start")
    dp.register_message_handler(forward, lambda m: m.forward_from or m.forward_from_chat, content_types="any")
    dp.register_message_handler(user_id, commands="id", chat_type="private")
    dp.register_message_handler(chat_id, commands="id")
    dp.register_message_handler(user_id, content_types="any", chat_type="private")
    dp.register_inline_handler(inline)
