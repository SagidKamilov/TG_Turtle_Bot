from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher
from Telegram_Turtle_Bot.sorted import bot
from Telegram_Turtle_Bot.keyboards.keyboard import full_keyboard, inline_button_one, inline_button_two
from Telegram_Turtle_Bot.commands_bot import Schedule


class FSMclient(StatesGroup):
    log_in = State()
    enter_group = State()


async def start_reg(message: types.Message):
    # if message.chat.type == 'private':
    await FSMclient.log_in.set()
    await bot.send_message(message.chat.id, '👀 Привет, перед использованием бота давай я помогу в нем разобраться.',
                               reply_markup=inline_button_two())


async def stop_reg(call_back: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.finish()
    await bot.edit_message_text('Как скажешь 🐢\nВот список команд: ', call_back.message.chat.id, call_back.message.message_id)
    # await bot.send_message(call_back.from_user.id, 'Как скажешь)\nВот список команд:')


async def default_func(call_back: types.CallbackQuery):
    await FSMclient.next()
    await bot.edit_message_text('✏ Напиши в какой ты группе.', call_back.message.chat.id, call_back.message.message_id)
    # await bot.send_message(call_back.from_user.id, '✏ Напиши в какой ты группе.')


async def enter_group(message: types.Message, state: FSMContext):
    schedule = Schedule()
    if schedule.check_group(group=message.text.upper()):
        await bot.send_message(message.from_user.id, 'Регистрация завершена, держи клавиатуру!',
                               reply_markup=full_keyboard(message.text.upper()))
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, '[🚫] Не могу найти такую группу, проверь пожалуйста, '
                                                     'правильно ли ты написал группу.', reply_markup=inline_button_one())


def register_handlers_one_client(dp: Dispatcher):
    dp.register_message_handler(start_reg, lambda message: message.chat.type == 'private',
                                Text(equals=['Начать', 'Регистрация'], ignore_case=True), state=None)
    dp.register_callback_query_handler(stop_reg, text='No', state='*')
    dp.register_message_handler(stop_reg, Text(equals=['Я больше не хочу регистрироваться', 'Завершить'],
                                               ignore_case=True), state='*')
    dp.register_callback_query_handler(default_func, text='Yeah', state=FSMclient.log_in)
    dp.register_message_handler(enter_group, content_types='text', state=FSMclient.enter_group)
