from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Back to the primitive everywhere
# Get csv in DQL mode

def dql_keyboard() -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with two buttons: "Get whole CSV" and "Abandon ship".
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text='Get whole CSV', callback_data='get_csv'),
        InlineKeyboardButton(text='Abandon ship', callback_data='init_state')
    ])

    return keyboard


def dml_keyboard() -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with one button: "Abandon ship".
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text='Abandon ship', callback_data='init_state')
    ])

    return keyboard
