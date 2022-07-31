from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# class KeyBoardBot:
#     def __init__(self, group):
#         api_from_turtle_bot = API()
#         if group in api_from_turtle_bot.take_group_list()['group']:
#             self.group = group
#
#     def full_keyboard(self):
#         b1 = KeyboardButton(f'Пары {self.group}')
#         b2 = KeyboardButton(f'Пары на неделю {self.group}')
#         b3 = KeyboardButton('Помощь')
#         key_b = ReplyKeyboardMarkup(resize_keyboard=True).row(b1, b2).row(b3)
#         return key_b
#
#     @staticmethod
#     def inline_button_one():
#         button_cancel = InlineKeyboardButton(text='Закончить регистрацию', callback_data='None')
#         key_b = InlineKeyboardMarkup().add(button_cancel)
#         return key_b


def keyboard():
    button = KeyboardButton('Помощь')
    key_b = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    return key_b


def full_keyboard(group):
    button1 = KeyboardButton(f'Пары {group}')
    button2 = KeyboardButton(f'Пары на неделю {group}')
    button3 = KeyboardButton('Помощь')
    key_b = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2).row(button3)
    return key_b


def inline_button_one():
    button_cancel = InlineKeyboardButton(text='Закончить регистрацию', callback_data='No')
    key_b = InlineKeyboardMarkup().add(button_cancel)
    return key_b


def inline_button_two():
    button_yes = InlineKeyboardButton(text='Да, давай', callback_data='Yeah')
    button_no = InlineKeyboardButton(text='Нет, не надо', callback_data='No')
    key_b = InlineKeyboardMarkup().row(button_yes, button_no)
    return key_b

