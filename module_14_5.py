import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from crud_functions import initiate_db, get_all_products, add_product, add_user, is_included

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


# Создаем класс состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Создаем обычную клавиатуру
def create_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Рассчитать"))
    builder.add(types.KeyboardButton(text="Информация"))
    builder.add(types.KeyboardButton(text="Купить"))
    builder.add(types.KeyboardButton(text="Регистрация"))
    builder.adjust(2)  # Подгоняем клавиатуру под 2 кнопки в строке
    return builder.as_markup(resize_keyboard=True)  # Делаем клавиатуру адаптивной


# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = create_reply_keyboard()  # Создаем обычную клавиатуру
    await message.answer(
        "Привет! Я помогу тебе рассчитать норму калорий. Нажми кнопку 'Рассчитать', чтобы начать.",
        reply_markup=keyboard,
    )


# Обработчик для кнопки "Регистрация"
@dp.message(lambda message: message.text == "Регистрация")
async def sign_up(message: types.Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


# Обработчик для ввода имени пользователя
@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if is_included(username):  # Проверяем, существует ли пользователь
        await message.answer("Пользователь существует, введите другое имя:")
        return  # Остаемся в состоянии username

    await state.update_data(username=username)  # Сохраняем имя пользователя
    await message.answer("Введите свой email:")
    await state.set_state(RegistrationState.email)


# Обработчик для ввода email
@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)  # Сохраняем email
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


# Обработчик для ввода возраста
@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)  # Пытаемся преобразовать ввод в число
    except ValueError:
        await message.answer("Пожалуйста, введите число для возраста.")
        return  # Остаемся в состоянии age

    # Получаем все данные из состояния
    data = await state.get_data()
    username = data["username"]
    email = data["email"]

    # Добавляем пользователя в базу данных
    add_user(username, email, age)

    await message.answer("Регистрация завершена! Ваш баланс: 1000.")
    await state.clear()  # Завершаем машину состояний


# Остальные обработчики (для кнопок "Рассчитать", "Купить" и т.д.) остаются без изменений

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())