import os
from aiogram import Router, types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
CHANNEL_MASTER = os.getenv('BOT_MASTER')
router = Router()


@router.callback_query()
async def application_cons(callback: types.callback_query, bot: Bot):
    username = callback.data
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text="✅ Принять",
            callback_data=f"accept_{callback.from_user.id}"
        ),
        types.InlineKeyboardButton(
            text="❌ Отказать",
            callback_data=f"reject_{callback.from_user.id}"
        )
    )
    try:
        await bot.send_message(
            chat_id=CHANNEL_MASTER.lstrip('@'),  # Убираем @ для поиска по username
            #text=f"Пользователь @{list(username.split(":"))[1]} хочет вступить в телеграм-канал!",
            text="abba",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        print(e)
        pass
    await callback.answer("Заявка отправлена!")


@router.callback_query(lambda c: c.data.startswith("accept_") or c.data.startswith("reject_"))
async def handle_decision(callback: types.callback_query, bot: Bot):
    invitation_link = "WIP"
    action, user_id = callback.data.spllit("_")
    user_id = int(user_id)
    print(user_id)
    if action == "accept":
        try:
            await bot.send_message(
                chat_id=user_id,
                text=f"Ваша заявка на вступление в чат была одобрена! Одноразовая ссылка-приглашение: {invitation_link}"
            )
            await callback.answer("Заявка принята!")
        except Exception:
            pass
    else:
        await callback.answer("Заявка отклонена!")
