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









# Запуск процесса поллинга новых апдейтов
