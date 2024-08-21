from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = '7482210268:AAGOAnag6efrx0AqqKfVvlm-T3LeSLKXxB4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
but_calc = KeyboardButton('Рассчитать')
but_info = KeyboardButton('Информация')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(but_calc, but_info)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message_handler(text='Информация')
async def get_info(message):
    info = ('Программа расчёта количества килокалорий в сутки для Вас.\n'
            'Используется упрощённая формула Миффлина-Сан Жеора.\n'
            'Ограничения:\nвозраст — 13–80 лет,\nрост — от 140 см,\nвес — от 40 кг.')
    await message.answer(info, reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        if int(message.text) < 13:
            raise ValueError()
    except ValueError:
        await message.answer('Ошибка! Формула применима для лиц в возрасте от 13 до 80 лет.\nВведите свой возраст:')
        await UserState.age.set()
    else:
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост (в сантиметрах):')
        await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        if int(message.text) < 140:
            raise ValueError()
    except ValueError:
        await message.answer('Ошибка! Нижняя граница роста — 140 см.\nВведите свой рост (в сантиметрах):')
        await UserState.growth.set()
    else:
        await state.update_data(growth=message.text)
        await message.answer('Введите свой вес (в килограммах):')
        await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_gender(message, state):
    try:
        if int(message.text) < 40:
            raise ValueError()
    except ValueError:
        await message.answer('Ошибка! Нижняя граница веса — 40 кг.\nВведите свой вес (в килограммах):')
        await UserState.weight.set()
    else:
        await state.update_data(weight=message.text)
        await message.answer('Введите свой пол (М / Ж):')
        await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    try:
        if data['gender'].upper() == 'М':
            rg = 5
        elif data['gender'].upper() == 'Ж':
            rg = -161
        else:
            raise ValueError()
    except ValueError:
        await message.answer('Ошибка!\nВведите свой пол (М / Ж):')
        await UserState.gender.set()
    else:
        result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + rg
        await message.answer(f'Количество килокалорий в сутки для Вас: {result}')
        await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
