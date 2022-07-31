from aiogram import types
from Telegram_Turtle_Bot.sorted import bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from Telegram_Turtle_Bot.commands_bot import Schedule

schedule_day = Schedule()


async def commands_help(message: types.Message):
    await bot.send_message(message.chat.id, schedule_day.get_help())


async def couples_week(message: types.Message):
    await bot.send_message(message.chat.id, schedule_day.get_schedule(message.text.upper()[15:]))


async def couples(message: types.Message):
    await bot.send_message(message.chat.id, schedule_day.get_schedule(message.text.upper()[5:]))


async def calls_schedule(message: types.Message):
    await bot.send_message(message.chat.id, schedule_day.get_calls())


async def teacher_name(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def my_group(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def rm_keyboard(message: types.Message):
    pass
    # await bot.send_message(message.from_user.id, )


async def notice_group(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def delete_notice(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def see_on(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def url_teacher(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


async def contact(message: types.Message):
    pass
    # await bot.send_message(message.chat.id, )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_help, Text(equals='помощь', ignore_case=True), content_types='text')
    dp.register_message_handler(couples_week, lambda message: 'пары на неделю' in message.text.lower(),
                                content_types='text')
    dp.register_message_handler(couples, lambda message: 'пары' in message.text.lower(), content_types='text')
    dp.register_message_handler(calls_schedule, Text(equals='звонки', ignore_case=True), content_types='text')
    dp.register_message_handler(teacher_name, Text(equals='фио', ignore_case=True), content_types='text')
    dp.register_message_handler(my_group, Text(equals='моя группа', ignore_case=True), content_types='text')
    dp.register_message_handler(rm_keyboard, Text(equals='убрери клавиатуру', ignore_case=True), content_types='text')
    dp.register_message_handler(notice_group, Text(equals='уведомления', ignore_case=True), content_types='text')
    dp.register_message_handler(delete_notice, Text(equals='отписать', ignore_case=True), content_types='text')
    dp.register_message_handler(see_on, Text(equals='отображаться', ignore_case=True), content_types='text')
    dp.register_message_handler(url_teacher, Text(equals='ссылка', ignore_case='True'), content_types='text')
    dp.register_message_handler(contact, Text(equals='контакты', ignore_case=True), content_types='text')
