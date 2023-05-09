import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, json, string


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте рады вас приветствовать ')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС напишите ему:\nhttps://t.me/test_tik_produkty_bot')


@dp.message_handler(commands=['Режим_работы'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 9 до 23')


@dp.message_handler(commands=['Расположение'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Одинцово ,Белорусская 5 "Манго"')


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("Маты запрещены")
        await message.delete()

    # if message.text == 'Привет':
    #     await message.answer('Привет Катечка сладкая булочка')
    # elif message.text == 'Эй':
    #     await message.answer('Иди к черту кожаный мешок ')
# await message.replay(message.text)
#await message.send_message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
