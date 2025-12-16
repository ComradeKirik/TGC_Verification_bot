import os
from dotenv import load_dotenv
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

load_dotenv()
BOT_MASTER = os.getenv('BOT_MASTER')

@router.message(Command("start"))
async def send_request(message: types.Message):
    builder = InlineKeyboardBuilder()
    callback_data = f"{message.from_user.id}:{message.from_user.first_name}"
    if message.from_user.id != int(BOT_MASTER):
        builder.add(types.InlineKeyboardButton(
            text="Отправить заявку",
            callback_data=callback_data)
        )

        await message.answer(
            "Нажмите на кнопку, чтобы отправить заявку на вступление в телеграм-канал",
            reply_markup=builder.as_markup()
        )
    else:
        await message.answer("Благодарю за использование бота! По всем багам и предложениям обращаться к @TowarichKirik")