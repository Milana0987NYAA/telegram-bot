import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


bot = Bot(token='7528668027:AAGWo1ZfnzGgpHiHNo5GQJbldM20AluE0B4')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вітаю! Я бочонок, чим можу допомогти?')
    await message.reply('ЯК СПРАВИ?')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Я ТУТ! Чим можу допомогти?')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот зупиненор")
    