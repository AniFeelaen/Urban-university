from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import bot_key

storage = MemoryStorage()
bot = Bot(token= bot_key.TOKEN)

dp = Dispatcher(bot, storage= storage)
dp.middleware.setup(LoggingMiddleware())


# Группа состояний для хранения данных о возрасте, росте и весе
class UserState(StatesGroup):
    age = State() 
    growth = State()  
    weight = State()  


# Функция для начала работы с ботом и получения возраста
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью.\nДля начала введите свой возраст.")
    await UserState.age.set()


# Обработчик для получения возраста
@dp.message_handler(state=UserState.age)
async def set_age(message: types.Message, state):
    try:
        age = int(message.text)
        if age <= 6 or age > 90:
            raise ValueError('Неправильно указан возраст.')
        
        await state.update_data(age=age)
        await message.answer("Отлично! Теперь введи свой рост в сантиметрах:")
        await UserState.next()   
    except ValueError as e:
        await message.answer(f"Пожалуйста, введите корректный возраст: {e}")


# Обработчик для получения роста
@dp.message_handler(state=UserState.growth)
async def set_growth(message: types.Message, state):
    try:
        growth = float(message.text)
        if growth <= 50 or growth > 250:
            raise ValueError('Рост должен быть в пределах от 50 до 250 см.')
        
        await state.update_data(growth=growth)
        await message.answer("Теперь введи свой вес в килограммах:")
        await UserState.next()
    
    except ValueError as e:
        await message.answer(f"Пожалуйста, введите корректный рост: {e}")


# Обработчик для получения веса
@dp.message_handler(state=UserState.weight)
async def set_weight(message: types.Message, state):
    try:
        weight = float(message.text)
        if weight <= 20 or weight > 150:
            raise ValueError('Вес должен быть в пределах от 20 до 150 кг.')
        
        await state.update_data(weight=weight)
        await calculate_and_send_calories(message, state)
    
    except ValueError as e:
        await message.answer(f"Пожалуйста, введите корректный вес: {e}")


# Функция для расчета нормы калорий и отправки результата
async def calculate_and_send_calories(message: types.Message, state):
    data = await state.get_data()
    age = data['age']
    growth = data['growth'] 
    weight = data['weight']
    print(age,growth,weight)

    # Упрощенная формула Миффлина-Сан Жеора для женщин
    calories = (10 * weight) + (6.25 * growth) - (5 * age)
    calories2 = calories - 163

    await message.answer(f"Ваша норма калорий составляет примерно {calories} ккал в день.Если - Вы женщина ваша норма калорий составляет {calories2}ккал в день. ")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
    
