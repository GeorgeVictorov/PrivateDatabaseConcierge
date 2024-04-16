from aiogram.fsm.state import State, StatesGroup


class FSMUserMode(StatesGroup):
    """
    States group representing different modes for user interaction.

    Attributes:
        DQL_MODE (State): State representing Data Query Language mode.
        DML_MODE (State): State representing Data Manipulation Language mode.
    """
    DQL_MODE = State()
    DML_MODE = State()
