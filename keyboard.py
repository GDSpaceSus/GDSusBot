from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def getLevelsKeyboard(key1:str, key2:str, page:int):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='1', callback_data=f'sl_1_{key1}'), InlineKeyboardButton(text='2', callback_data=f'sl_2_{key1}'), InlineKeyboardButton(text='3', callback_data=f'sl_3_{key1}'), InlineKeyboardButton(text='4', callback_data=f'sl_4_{key1}'), InlineKeyboardButton(text='5', callback_data=f'sl_5_{key1}')],
            [InlineKeyboardButton(text='<', callback_data=f'sl_<_{key2}'), InlineKeyboardButton(text=f'{page}', callback_data=f'-'), InlineKeyboardButton(text='>', callback_data=f'sl_>_{key2}')],
        ]
    )
    return keyboard

def getLevelKeyboard(key1:str, key2:str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Comments', callback_data=f'ld_c_{key1}'), InlineKeyboardButton(text='Author', callback_data=f'ld_a_{key2}')]
        ]
    )
    return keyboard