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

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='5938405821:AAGuN2xdnUCdT_SzDeCyH4t1bBDA8TCWrY8', parse_mode='HTML')
# Диспетчер
dp = Dispatcher()
mylist = []
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")

@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")

@dp.message(Command("name"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")

""" @dp.message(F.text)
async def echo_with_time(message: types.Message):
    # Получаем текущее время в часовом поясе ПК
    time_now = datetime.now().strftime('%H:%M')
    # Создаём подчёркнутый текст
    added_text = html.underline(f"Создано в {time_now}")
    # Отправляем новое сообщение с добавленным текстом
    await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML") """

""" @dp.message(F.text)
async def extract_data(message: types.Message):
    data = {
        "url": "<N/A>",
        "email": "<N/A>",
        "code": "<N/A>"
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            # Неправильно
            # data[item.type] = message.text[item.offset : item.offset+item.length]
            # Правильно
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Пароль: {html.quote(data['code'])}"
    ) """

@dp.message(F.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message(Command('images'))
async def upload_photo(message: types.Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"
    # открытием файла через `open()`. Но, вообще говоря, этот способ
    # лучше всего подходит для отправки байтов из оперативной памяти
    # после проведения каких-либо манипуляций, например, редактированием через Pillow
    """ with open("buffer_emulation.jpg", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="image from buffer.jpg"
            ),
            caption="Изображение из буфера"
        )
        file_ids.append(result.photo[-1].file_id)

    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("image_from_pc.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id) """

    # Отправка файла по ссылке
    image_from_url = URLInputFile("https://avatars.mds.yandex.net/get-kinopoisk-image/1946459/2b36859a-0d2f-4076-8474-6793386c45a0/1920x")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("Отправленные файлы:\n"+"\n".join(file_ids))

@dp.message(Command("hidden_link"))
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, mylist=mylist)



if __name__ == "__main__":
    asyncio.run(main())