import os
from aiogram import Router, types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv


load_dotenv()
CHANNEL_MASTER = os.getenv('BOT_MASTER')
CHANNEL_ID = os.getenv('CHANNEL_ID')
router = Router()


@router.callback_query()
async def application_cons(callback: types.CallbackQuery, bot: Bot):
    if callback.data.startswith("accept_") or callback.data.startswith("reject_"):
        print("Ошибка предотвращена")
        await handle_decision(callback, bot)
        return None

    username = callback.data
    print(username)
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
            chat_id=CHANNEL_MASTER.lstrip('@'),
            text=f"Пользователь @{list(username.split(':'))[1]} хочет вступить в телеграм-канал!",
            reply_markup=builder.as_markup()
        )
    except ValueError:
        pass
    await callback.answer("Заявка отправлена!")

async def create_invite_link(bot: Bot):
    link = await bot.create_chat_invite_link(chat_id=CHANNEL_ID, member_limit=1)
    return link.invite_link

@router.callback_query(lambda c: c.data.startswith("accept_") or c.data.startswith("reject_"))
async def handle_decision(callback: types.CallbackQuery, bot: Bot):
    action, user_id = callback.data.split("_")
    user_id = int(user_id)
    if action == "accept":
        try:
            print(1)
            link = await create_invite_link(bot)
            print(2)
            await bot.send_message(
                chat_id=user_id,
                text=f"Ваша заявка на вступление в чат была одобрена! Одноразовая ссылка-приглашение: {link}"
            )
            await callback.answer("Заявка принята!")
        except Exception as e:
            print(e)
            pass
    else:
        await callback.answer("Заявка отклонена!")
