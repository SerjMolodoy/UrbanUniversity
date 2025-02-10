import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = 'Апи'  # Ваш токен

# Используем DefaultBotProperties для настройки parse_mode
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()  # Хранилище состояний
dp = Dispatcher(storage=storage)

# Определяем состояния
class UserState(StatesGroup):
    age = State()  # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я помогу тебе рассчитать норму калорий. Напиши 'Calories', чтобы начать.")

# Обработчик для начала цепочки состояний
@dp.message(lambda message: message.text == "Calories")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)  # Устанавливаем состояние age

# Обработчик для ввода возраста
@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserState.growth)  # Устанавливаем состояние growth

# Обработчик для ввода роста
@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserState.weight)  # Устанавливаем состояние weight

# Обработчик для ввода веса и расчета калорий
@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()  # Получаем все данные

    # Преобразуем данные в числа
    try:
        age = int(data["age"])
        growth = int(data["growth"])
        weight = int(data["weight"])
    except ValueError:
        await message.answer("Пожалуйста, вводите только числа. Начните заново, написав 'Calories'.")
        await state.clear()  # Сбрасываем состояние
        return

    # Формула Миффлина - Сан Жеора для мужчин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5

    # Отправляем результат
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.finish()  # Завершаем машину состояний

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())