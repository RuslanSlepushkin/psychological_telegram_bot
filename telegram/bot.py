from create_bot import dp
from aiogram import executor
from handlers import handler_base, handler_worklist, handler_abcmodel, handler_fallingarrow, handler_bai, \
    handler_emotions, handler_history, handler_show, handler_delete


handler_base.register_handlers_base(dp)
handler_worklist.register_handlers_worklist(dp)
handler_abcmodel.register_handlers_abcmodel(dp)
handler_fallingarrow.register_handlers_fallingarrow(dp)
handler_bai.register_handlers_bai(dp)
handler_emotions.register_handlers_emotions(dp)
handler_history.register_handlers_history(dp)
handler_show.register_handlers_show(dp)
handler_delete.register_handlers_delete(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)