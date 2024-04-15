from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Back to the primitive everywhere
# Get csv in DQL mode

def dql_keyboard() -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with two buttons: "Get whole CSV" and "Make a new query".
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text="Get whole CSV", callback_data="get_csv"),
        InlineKeyboardButton(text="Make a new query", callback_data="new_query")
    ])

    return keyboard
