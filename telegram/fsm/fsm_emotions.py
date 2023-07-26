from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMEmotions(StatesGroup):
    question_1 = State()
    question_2 = State()
    push = State()


