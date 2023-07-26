from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.fsm.fsm_worklist import FSMWorklist
from telegram.keyboards.keybords_default import get_next_kb, get_ok_kb
from telegram.data_base.db_worklist import get_question_worklist, down_worklist, down_user


# @dp.message_handler(Text(equals='Сформувати запит', ignore_case=True), state=None)
async def get_request(message: types.Message):
    await FSMWorklist.question_1.set()
    await message.answer(text=await get_question_worklist(1))


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.message_handler(state=FSMWorklist.question_1)
async def get_question_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(2))


# @dp.message_handler(state=FSMWorklist.question_2)
async def get_question_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(3))


# @dp.message_handler(state=FSMWorklist.question_3)
async def get_question_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(4))


# @dp.message_handler(state=FSMWorklist.question_4)
async def get_question_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(5))


# @dp.message_handler(state=FSMWorklist.question_5)
async def get_question_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(6))


# @dp.message_handler(state=FSMWorklist.question_6)
async def get_question_6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_6'] = message.text
    await FSMWorklist.next()
    await message.answer(text=await get_question_worklist(7))


# @dp.message_handler(state=FSMWorklist.question_7)
async def get_question_7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_7'] = message.text
        data_dict = dict(data.items())
        await down_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await down_worklist(message.from_user.id, data_dict)
    await state.finish()
    await message.answer(text="Тисни далі для проходження ABC-моделі", reply_markup=get_next_kb())


def register_handlers_worklist(dp: Dispatcher):
    dp.register_message_handler(get_request, Text(equals='Сформувати запит', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(get_question_1, state=FSMWorklist.question_1)
    dp.register_message_handler(get_question_2, state=FSMWorklist.question_2)
    dp.register_message_handler(get_question_3, state=FSMWorklist.question_3)
    dp.register_message_handler(get_question_4, state=FSMWorklist.question_4)
    dp.register_message_handler(get_question_5, state=FSMWorklist.question_5)
    dp.register_message_handler(get_question_6, state=FSMWorklist.question_6)
    dp.register_message_handler(get_question_7, state=FSMWorklist.question_7)
