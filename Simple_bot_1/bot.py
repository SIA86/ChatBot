import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, different_types
from handlers import group_games,usernames, checkin
from middlewares.weekend import WeekendCallbackMiddleware

# Запуск бота
async def main():
    bot = Bot(token='5938405821:AAGuN2xdnUCdT_SzDeCyH4t1bBDA8TCWrY8')
    dp = Dispatcher()
    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())
    dp.include_routers(checkin.router)
    
    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())