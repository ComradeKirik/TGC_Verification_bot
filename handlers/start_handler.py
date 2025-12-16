from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def send_request(message: types.Message):
    builder = InlineKeyboardBuilder()
    callback_data = f"{message.from_user.id}:{message.from_user.first_name}"

    builder.add(types.InlineKeyboardButton(
        text="Отправить заявку",
        callback_data=callback_data)
    )

    await message.answer(
        "Нажмите на кнопку, чтобы отправить заявку на вступление в телеграм-канал",
        reply_markup=builder.as_markup()
    )
