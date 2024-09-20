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

dp = Dispatcher()

@dp.callback_query(F.data == "num_decr")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str("hi"))