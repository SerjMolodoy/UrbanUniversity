import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from crud_functions import initiate_db, get_all_products, add_product

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = 'Апи'  # Замените на ваш токен

# Используем DefaultBotProperties для настройки parse_mode
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()  # Хранилище состояний
dp = Dispatcher(storage=storage)

# Инициализация базы данных при запуске бота
initiate_db()


# Добавляем несколько продуктов в базу данных (если их еще нет)
def populate_db():
    products = [
        {"title": "Product1", "description": "Описание 1", "price": 100},
        {"title": "Product2", "description": "Описание 2", "price": 200},
        {"title": "Product3", "description": "Описание 3", "price": 300},
        {"title": "Product4", "description": "Описание 4", "price": 400},
    ]

    for product in products:
        add_product(product["title"], product["description"], product["price"])


# Запускаем функцию для добавления продуктов в базу данных
populate_db()


# Создаем обычную клавиатуру
def create_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Рассчитать"))
    builder.add(types.KeyboardButton(text="Информация"))
    builder.add(types.KeyboardButton(text="Купить"))
    builder.adjust(2)  # Подгоняем клавиатуру под 2 кнопки в строке
    return builder.as_markup(resize_keyboard=True)  # Делаем клавиатуру адаптивной


# Создаем инлайн-клавиатуру для выбора продукта
def create_buying_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Product1",
        callback_data="product_buying",
    ))
    builder.add(types.InlineKeyboardButton(
        text="Product2",
        callback_data="product_buying",
    ))
    builder.add(types.InlineKeyboardButton(
        text="Product3",
        callback_data="product_buying",
    ))
    builder.add(types.InlineKeyboardButton(
        text="Product4",
        callback_data="product_buying",
    ))
    builder.adjust(2)  # Подгоняем клавиатуру под 2 кнопки в строке
    return builder.as_markup()


# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = create_reply_keyboard()  # Создаем обычную клавиатуру
    await message.answer(
        "Привет! Я помогу тебе рассчитать норму калорий. Нажми кнопку 'Рассчитать', чтобы начать.",
        reply_markup=keyboard,
    )


# Обработчик для кнопки "Рассчитать"
@dp.message(lambda message: message.text == "Рассчитать")
async def main_menu(message: types.Message):
    keyboard = create_buying_inline_keyboard()  # Используем create_buying_inline_keyboard
    await message.answer("Выберите опцию:", reply_markup=keyboard)


# Обработчик для кнопки "Купить"
@dp.message(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()  # Получаем все продукты из базы данных

    for product in products:
        await message.answer_photo(
            photo="https://via.placeholder.com/150",  # Замените на реальный URL изображения
            caption=f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}",
        )

    keyboard = create_buying_inline_keyboard()
    await message.answer("Выберите продукт для покупки:", reply_markup=keyboard)


# Обработчик для покупки продукта
@dp.callback_query(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Подтверждаем обработку callback


# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())