from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Telegram_Turtle_Bot.keyboards.keyboard import full_keyboard, inline_button_one, inline_button_two
from Telegram_Turtle_Bot.TurtleAPI import API

storage = MemoryStorage()
Token = '5572913974:AAF6Dat2900wj3wiWG9WfChx_wQxgtvixqU'
bot = Bot(token=Token)
dp = Dispatcher(bot, storage=storage)


class FSMcontin(StatesGroup):
    log_in = State()
    group_name = State()
    answer_ = State()


SPIS = [
    'Начать',
    'Регистрация'
]


@dp.message_handler(Text(equals=SPIS, ignore_case=True))
@dp.message_handler(commands='start', state=None)
async def start(message: types.Message):
    await FSMcontin.log_in.set()
    await bot.send_message(message.from_user.id, 'Привет, перед использованием бота давай я помогу в нем разобраться.',
                           reply_markup=inline_button_two())


@dp.callback_query_handler(text="None", state="*")
@dp.message_handler(Text(equals='нет', ignore_case=True), state="*")
async def function4(call_back: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.finish()
    await bot.send_message(call_back.from_user.id, 'ok, bay')
    await call_back.answer('OK')


@dp.callback_query_handler(text='Yeah', state=FSMcontin.log_in)
@dp.message_handler(content_types=['text'], state=FSMcontin.log_in)
async def function1(call_back: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['log_in'] = 'Да'
    await FSMcontin.next()
    await call_back.answer(text='OK')
    await bot.send_message(call_back.from_user.id, 'Отлично! Введите название группы...')
    await bot.edit_message_text('ok', chat_id=call_back.message.chat.id, message_id=call_back.message.message_id)


@dp.message_handler(content_types=['text'], state=FSMcontin.group_name)
async def function2(message: types.Message):
    await bot.send_message(message.from_user.id, 'неа')


@dp.message_handler(content_types='text', state=FSMcontin.answer_)
async def function3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            await bot.send_message(message.from_user.id, 'Регистрация завершена, держи',
                                   reply_markup=full_keyboard(group=data['group_name']))
        else:
            await bot.send_message(message.from_user.id, 'Регистрация завершена)',
                                   reply_markup=full_keyboard(None))
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
