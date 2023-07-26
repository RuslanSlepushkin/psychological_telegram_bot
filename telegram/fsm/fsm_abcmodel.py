from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMABCModel(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    arrow = State()

