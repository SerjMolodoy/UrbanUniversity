import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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


# Создаем обычную клавиатуру
def create_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Рассчитать"))
    builder.add(types.KeyboardButton(text="Информация"))
    builder.adjust(2)  # Подгоняем клавиатуру под 2 кнопки в строке
    return builder.as_markup(resize_keyboard=True)  # Делаем клавиатуру адаптивной


# Создаем инлайн-клавиатуру
def create_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Рассчитать норму калорий",
        callback_data="calories",
    ))
    builder.add(types.InlineKeyboardButton(
        text="Формулы расчёта",
        callback_data="formulas",
    ))
    builder.adjust(1)  # Подгоняем клавиатуру под 1 кнопку в строке
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
    keyboard = create_inline_keyboard()  # Создаем инлайн-клавиатуру
    await message.answer("Выберите опцию:", reply_markup=keyboard)


# Обработчик для кнопки "Формулы расчёта"
@dp.callback_query(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора для мужчин:\n"
        "Калории = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст в годах) + 5\n\n"
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "Калории = (10 × вес в кг) + (6.25 × рост в см) - (5 × возраст в годах) - 161"
    )
    await call.message.answer(formula_text)
    await call.answer()  # Подтверждаем обработку callback


# Обработчик для кнопки "Рассчитать норму калорий"
@dp.callback_query(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())  # Убираем клавиатуру
    await state.set_state(UserState.age)  # Устанавливаем состояние age
    await call.answer()  # Подтверждаем обработку callback


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
        await message.answer("Пожалуйста, вводите только числа. Начните заново, написав 'Рассчитать'.")
        await state.clear()  # Сбрасываем состояние
        return

    # Формула Миффлина - Сан Жеора для мужчин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5

    # Отправляем результат
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.finish()  # Завершаем машину состояний


# Обработчик для кнопки "Информация"
@dp.message(lambda message: message.text == "Информация")
async def send_info(message: types.Message):
    await message.answer(
        "Этот бот помогает рассчитать норму калорий по формуле Миффлина - Сан Жеора. "
        "Нажмите кнопку 'Рассчитать', чтобы начать.",
        reply_markup=create_reply_keyboard(),  # Возвращаем клавиатуру
    )


# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
