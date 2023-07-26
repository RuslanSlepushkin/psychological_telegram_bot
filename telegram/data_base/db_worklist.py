import json

from datetime import datetime
from telegram.data_base.db import get_create_connection


async def get_question_worklist(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT question_text FROM bot_questionsworklist WHERE id = $1", num)
    return value


async def get_text_worklist(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT text FROM bot_questionsworklist WHERE id = $1", num)
    return value


async def down_user(user_id: int, user_name: str, first_name: str) -> None:
    conn = await get_create_connection()
    await conn.execute("""
         INSERT INTO bot_tguser (user_id, user_name, first_name) VALUES ($1, $2, $3)
         ON CONFLICT (user_id) DO UPDATE SET user_name = EXCLUDED.user_name, first_name = EXCLUDED.first_name
     """, user_id, user_name, first_name)


async def down_worklist(user_id: int, data: dict) -> None:
        conn = await get_create_connection()
        time = datetime.now().replace(second=0, microsecond=0)
        json_data = json.dumps(data)
        await conn.execute("INSERT INTO bot_answersworklist (user_id, answers, date) VALUES ($1, $2, $3)",
                           user_id, json_data, time)


async def load_pdf_worklist_answers(user_id: int) -> dict:
    conn = await get_create_connection()
    value = await conn.fetchval(f"SELECT answers FROM bot_answersworklist WHERE user_id = "
                                f"{user_id} ORDER BY id DESC LIMIT 1;")
    return value


async def load_pdf_worklist_questions() -> list:
    conn = await get_create_connection()
    values = await conn.fetch(f"SELECT question_text FROM bot_questionsworklist")
    question_texts = [row['question_text'] for row in values]
    return question_texts
