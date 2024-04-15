import logging
from states.states import FSMUserMode
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ContentType, CallbackQuery
from lexicon.lexicon import MESSAGES
from keyboards.keyboards import dql_keyboard
from filters.admin import IsAdmin

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
    await message.answer(MESSAGES["/dql"], parse_mode='HTML')
    await state.set_state(FSMUserMode.DQL_MODE)


@router.message(IsAdmin(), Command('dml'), StateFilter(default_state))
async def dml_mode(message: Message, state: FSMContext):
    """
    Handle the /dml command to enter Data Manipulation Language mode.
    This command is available only for admins.
    """
    await message.answer(MESSAGES["/dml"], parse_mode='HTML')
    await state.set_state(FSMUserMode.DML_MODE)
