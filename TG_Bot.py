from aiogram.utils import executor
from Telegram_Turtle_Bot.sorted import dp
from Telegram_Turtle_Bot.handlers import registration, group


registration.register_handlers_one_client(dp)
group.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates='True')
