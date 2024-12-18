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
button3 = KeyboardButton( text= 'Купить')
menu.row(button, button2, button3)
# menu.add(button, button2)
menu.resize_keyboard=True

#создание инлайн клавиатуры с 2 кнопками

inline = InlineKeyboardMarkup(row_width=2)
inline.add(
    types.InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories' ),
    types.InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas'  ),
    types.InlineKeyboardButton(text = 'Купить!', callback_data='ссылка'  ),
    types.InlineKeyboardButton(text = 'Назад', callback_data='back_to_catalog'  )
)
inline.resize_keyboard=True

inline2 = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    inline2.insert(InlineKeyboardButton(f'Product{i}', callback_data=f'product_buying{i}'))
inline2.resize_keyboard=True
# reply_markup_inline = InlineKeyboardMarkup(inline2)

class UserState(StatesGroup):
    age = State() 
    growth = State()  
    weight = State()  

# Функция для начала работы с ботом и получения возраста
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer(
        f"Привет!{message.from_user.username} Я бот помогающий твоему здоровью.", reply_markup = menu)

#обработка обычной клавиатуры на клик по Рассчитать
@dp.message_handler(Text(equals='Рассчитать'))
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = inline) 

# Обработчик нажатия кнопки "Информация"
@dp.message_handler(Text(equals='Информация'))
async def info_menu(message: types.Message):
    await message.answer('Это информация.', reply_markup=menu)
    
@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call):
    await call.message.answer('формула для мужчин - (10 * вес) + (6.25 * рост) - (5 * возраст),\nформула для женщин - (10 * вес) + (6.25 * рост) - (5 * возраст) - 163')

# Обработчик нажатия кнопки "Купить"
@dp.message_handler(Text(equals='Купить'))
async def get_buying_list(message):
    for i in range(1, 5):
        # Отправляем информацию о продукте
        # await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        # Отправляем картинку продукта (замените на реальные пути к изображениям)
        with open(f'module_14/{i}.png', "rb") as img:
            await message.answer_photo(img, caption=f'Название: Алкозельцер{i} | Описание: Препарат номер{i} | Цена: {i * 100}')
    # Отправляем inline-меню после информации о продуктах
    await message.answer('Выберите продукт для покупки:', reply_markup=inline2)
    
    
    
# Обработчик коллбэка "product_buying"
@dp.callback_query_handler(Text(startswith='product_buying'))
async def send_confirm_message(call: types.message):
    await call.answer("Вы успешно приобрели продукт!")

@dp.callback_query_handler(Text(equals='calories'))
async def back(call: types.Message):
   await call.message.answer( 'Для начала введите свой возраст')
 
#обработка кнопки Назад
@dp.callback_query_handler(Text(equals='back_to_catalog'))
async def set_age(call: types.Message):
    await call.message.answer(
        f"Привет!{call.message.from_user.username} Я бот помогающий твоему здоровью.", reply_markup = menu)
    
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
    await message.reply(f"Здравствуйте!, {message.from_user.username}")

@dp.message_handler()
async def default_message_handler(message: types.Message):
    await message.answer("Я пока не знаю, как отвечать на такие сообщения. Попробуйте ввести команду /start.")
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)