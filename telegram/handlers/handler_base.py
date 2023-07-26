from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from telegram.keyboards.keyboard_inline import get_url_kb
from telegram.data_base.db_worklist import get_text_worklist
from telegram.keyboards.keybords_default import get_ok_kb, get_choice_kb, get_choice_homework_kb


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=f"Привіт, {message.from_user.first_name}, {await get_text_worklist(1)}",
                         reply_markup=get_ok_kb())
    await message.delete()


# @dp.message_handler(Text(equals="OK", ignore_case=True))
async def choice(message: types.Message):
    await message.answer(text="Тепер дозволь мені дізнатися, яка мета твого перебування тут",
                         reply_markup=get_choice_kb())
    await message.delete()


# @dp.message_handler(Text(equals="Домашнє завдання", ignore_case=True))
async def homework(message: types.Message):
    await message.answer(text="Обери завдання",
                         reply_markup=get_choice_homework_kb())
    await message.delete()


# @dp.message_handler(Text(equals="Більше про когнітивно-поведінкову терапію", ignore_case=True))
async def more_kpt(message: types.Message):
    await message.answer(text=await get_text_worklist(3), reply_markup=get_ok_kb())
    await message.delete()


# @dp.message_handler(commands=['contact'])
async def url_contact(message: types.Message):
    await message.answer(text='Contact', reply_markup=get_url_kb())
    await message.delete()


def register_handlers_base(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(choice, Text(equals='OK', ignore_case=True))
    dp.register_message_handler(homework, Text(equals="Домашнє завдання", ignore_case=True))
    dp.register_message_handler(more_kpt, Text(equals="Більше про когнітивно-поведінкову терапію", ignore_case=True))
    dp.register_message_handler(url_contact, commands=['contact'])
