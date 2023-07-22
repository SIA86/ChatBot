import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram import types
from aiogram import html
from aiogram import F
from datetime import datetime
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.markdown import hide_link
from aiogram.filters import Text

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='5938405821:AAGuN2xdnUCdT_SzDeCyH4t1bBDA8TCWrY8', parse_mode='HTML')
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dp.message(Text("С пюрешкой"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(lambda message: message.text == "Без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    asyncio.run(main())