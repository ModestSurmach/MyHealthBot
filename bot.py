 #API_TOKEN = '7882865603:AAGtWfxHbaMfPdD2y6lkoKwoTovJJuQS0Ek'
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import pandas as pd
import numpy as np
from email.message import EmailMessage
import smtplib



my_email = EmailMessage()

my_email["from"] = "modest"
my_email["to"] = 'mosurmach@yandex.ru'
my_email['subject'] = 'hello'
my_email.set_content("hey")

def send_email():
    with smtplib.SMTP(host='89.111.174.216', port=5050) as smtp_server:
        smtp_server.ehlo()
        smtp_server.send_message(my_email)

#from table import tableDoc

token = '7882865603:AAGtWfxHbaMfPdD2y6lkoKwoTovJJuQS0Ek'

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
    token=token,
    default=DefaultBotProperties(
        parse_mode= ParseMode.HTML
        # тут ещё много других интересных настроек
    )
)
bot =Bot(token=token, parsparse_mode="HTML")

# Диспетчер
dp = Dispatcher()


lineA = "Line a"




## Старт 
@dp.message(Command("start"))
async def cmd_numbers(message: types.Message):
    await message.answer("Добрый день", reply_markup=get_keyboard_start())

def get_keyboard_start():
    buttons = [
        [types.InlineKeyboardButton(text="Узнать расписание", callback_data="Find_schedule")],
        [types.InlineKeyboardButton(text="Записаться на прием", callback_data="Make_appointment")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@dp.callback_query(F.data == "Find_schedule")
async def find_schedule(callback: types.CallbackQuery):
    await callback.message.answer(send_email())


@dp.callback_query(F.data == "Make_appointment")
async def make_appointment(callback: types.CallbackQuery):
    await callback.message.answer(str("Пока"))






# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())