import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = 'Апи'  # Ваш токен

# Используем DefaultBotProperties для настройки parse_mode
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()  # Dispatcher больше не принимает бота в конструкторе

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    # Отправляем сообщение в чат
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

# Обработчик всех остальных сообщений
@dp.message()
async def all_messages(message: types.Message):
    # Отправляем сообщение в чат
    await message.answer('Введите команду /start, чтобы начать общение.')

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())