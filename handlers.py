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
from bot import dp
 



@dp.callback_query(F.data == "Find_schedule")
async def find_schedule(callback: types.CallbackQuery):
    await callback.message.answer(lineA)


@dp.callback_query(F.data == "Make_appointment")
async def make_appointment(callback: types.CallbackQuery):
    await callback.message.answer(str("Пока"))