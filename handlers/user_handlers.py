from states.states import FSMUserMode
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ContentType, CallbackQuery, BufferedInputFile
from lexicon.lexicon import MESSAGES, INFO
from keyboards.keyboards import dql_keyboard, dml_keyboard
from database.dql import select_data, clear_cached_data
from filters.admin import IsAdmin
from services.parse_data import parse_sql_data, generate_filename, data_to_csv

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def start_command(message: Message):
    """
    Handle the /start command to initiate the bot and send a welcome message.
    """
    await message.answer(MESSAGES["/start"], parse_mode='HTML')


@router.message(Command('cancel'), ~StateFilter(default_state))
async def cancel_command(message: Message, state: FSMContext):
    """
    Handle the /cancel command to return the user to the default state.
    """
    await message.answer(MESSAGES["/start"], parse_mode='HTML')
    await state.set_state(default_state)


@router.message(Command('dql'), StateFilter(default_state))
async def dql_mode(message: Message, state: FSMContext):
    """
    Handle the /dql command to enter Data Query Language mode.
    """
    await message.answer(MESSAGES["/dql"], reply_markup=dml_keyboard(), parse_mode='HTML')
    await state.set_state(FSMUserMode.DQL_MODE)


@router.message(IsAdmin(), Command('dml'), StateFilter(default_state))
async def dml_mode(message: Message, state: FSMContext):
    """
    Handle the /dml command to enter Data Manipulation Language mode.
    This command is available only for admins.
    """
    await message.answer(MESSAGES["/dml"], reply_markup=dml_keyboard(), parse_mode='HTML')
    await state.set_state(FSMUserMode.DML_MODE)


@router.message(F.content_type == ContentType.TEXT, StateFilter(FSMUserMode.DQL_MODE))
async def process_dql_query(message: Message, state: FSMContext):
    """
    Process a DQL query provided in a text message.
    """
    query = message.text.strip()
    await state.update_data(query=query)

    columns, rows = select_data(query)
    if columns and rows:
        parsed_data = parse_sql_data(columns, rows)
        await message.answer(parsed_data, parse_mode='HTML')
        await message.answer(INFO['action'], parse_mode='HTML', reply_markup=dql_keyboard())
    else:
        await message.reply(INFO['no_data'], parse_mode='HTML')


@router.callback_query(F.data.in_({'get_csv', 'init_state'}), StateFilter(FSMUserMode.DQL_MODE))
async def process_keyboard_actions(callback_query: CallbackQuery, state: FSMContext):
    """
    Process actions triggered by keyboard buttons for DQL mode.

    Parameters:
        callback_query (CallbackQuery): The callback query object.
        state (FSMContext): The FSM state context.

    """
    action = callback_query.data

    if action == 'init_state':
        await callback_query.message.edit_text(INFO['abandon'], parse_mode='HTML')
        await state.set_state(default_state)
        await start_command(callback_query.message)

    elif action == 'get_csv':
        query_data = await state.get_data()
        query = query_data.get('query')

        columns, rows = select_data(query)

        clear_cached_data()

        if columns and rows:
            csv_data = data_to_csv(columns, rows)
            file_name = generate_filename(rows)
            await callback_query.message.edit_text(INFO['csv_text'], parse_mode='HTML')
            await callback_query.message.answer_document(BufferedInputFile(csv_data.encode(), filename=file_name))
