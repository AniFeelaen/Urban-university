from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import bot_key

storage = MemoryStorage()
bot = Bot(token= bot_key.TOKEN)

dp = Dispatcher(bot, storage= storage)
   
@dp.message_handler(commands = ["start"] )
async def start (message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    # await message.reply
@dp.message_handler()
async def all_message (message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)

    
    
    
    
