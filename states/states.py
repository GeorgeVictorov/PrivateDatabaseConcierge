from aiogram.fsm.state import State, StatesGroup


class FSMUserMode(StatesGroup):
    DQL_MODE = State()
    DML_MODE = State()
