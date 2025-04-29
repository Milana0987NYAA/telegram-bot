import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Messege

bot = Bot(token='7850661812:AAFpzahnZC60IDy_lXyx2NBbkxHS6IyTNt4')
dp = Dispatcher(bot)



@dp.message()
asynx def cmd_start(message: Message):
    await message.answer('Вітаю! Я бочонок, чим можу допомогти?')
    await message.reply('ЯК СПРАВИ?')


asynx def main() :
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    print('Bot started')