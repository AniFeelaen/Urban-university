from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import bot_key
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

storage = MemoryStorage()
#доступ к боту
bot = Bot(token= bot_key.TOKEN)
dp = Dispatcher(bot, storage= storage)
dp.middleware.setup(LoggingMiddleware())

menu = ReplyKeyboardMarkup()
button = KeyboardButton( text= 'Рассчитать')
button2 = KeyboardButton( text= 'Информация')
menu.add(button)
menu.add(button2)
# menu.add(button, button2)
menu.resize_keyboard=True

#создание инлайн клавиатуры с 2 кнопками
inline = InlineKeyboardMarkup()
inline_button1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories' )
inline_button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas'  )
inline.add(inline_button1)
inline.add(inline_button2)
inline.resize_keyboard=True

# inline = InlineKeyboardMarkup().row(
#     types.InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories' ),
#     types.InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas'  ),
# )

# Группа состояний для хранения данных о возрасте, росте и весе
class UserState(StatesGroup):
    age = State() 
    growth = State()  
    weight = State()  
    
#обработка обычной клавиатуры на клик по Рассчитать
@dp.message_handler(Text(equals='Рассчитать'))
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = inline) 
@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call):
    await call.message.answer('формула для мужчин - (10 * вес) + (6.25 * рост) - (5 * возраст),\nформула для женщин - (10 * вес) + (6.25 * рост) - (5 * возраст) - 163')
# 'формула для женщин - (10 * вес) + (6.25 * рост) - (5 * возраст) - 163') 
    
    
# Функция для начала работы с ботом и получения возраста
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    # reply_markup = ReplyKeyboardMarkup(kb, resize_keyboard=True)
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью.", reply_markup = menu)
    # await UserState.age.set()
    # Text(equals='привет') 
    # state=UserState.age
@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.Message):
   await call.message.answer( 'Для начала введите свой возраст')
   await UserState.age.set()

# Обработчик для получения возраста
@dp.message_handler(state=UserState.age)
async def set_age(message: types.Message, state):
    try:
        age = int(message.text)
        if age <= 6 or age > 90:
            raise ValueError('Неправильно указан возраст, введите возраст от 6 до 90.')
        
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

# Обработчик всех сообщений, кроме команд
@dp.message_handler(Text(equals='привет'))
async def greetings(message: types.Message):
    await message.reply("Здравствуйте!")

@dp.message_handler()
async def default_message_handler(message: types.Message):
    await message.answer("Я пока не знаю, как отвечать на такие сообщения. Попробуйте ввести команду /start.")
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)