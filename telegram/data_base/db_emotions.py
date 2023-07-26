import json

from datetime import datetime
from telegram.data_base.db import get_create_connection


async def down_user(user_id: int, user_name: str, first_name: str) -> None:
    conn = await get_create_connection()
    await conn.execute("""
         INSERT INTO bot_tguser (user_id, user_name, first_name) VALUES ($1, $2, $3)
         ON CONFLICT (user_id) DO UPDATE SET user_name = EXCLUDED.user_name, first_name = EXCLUDED.first_name
     """, user_id, user_name, first_name)


async def get_question_emotions(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT question_text FROM bot_questionsemotions WHERE id = $1", num)
    return value


async def get_text_emotions(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT text FROM bot_questionsemotions WHERE id = $1", num)
    return value


async def down_emotions(user_id: int, data: dict) -> None:
        conn = await get_create_connection()
        time = datetime.now().replace(second=0, microsecond=0)
        json_data = json.dumps(data)
        await conn.execute("INSERT INTO bot_answersemotions (user_id, answers, date) VALUES ($1, $2, $3)",
                           user_id, json_data, time)


async def load_pdf_emotions_answers(user_id: int) -> dict:
    conn = await get_create_connection()
    value = await conn.fetchrow(f"SELECT answers, date FROM bot_answersemotions WHERE user_id = "
                                f"{user_id} ORDER BY id DESC LIMIT 1;")
    return value


async def load_pdf_emotions_questions() -> list:
    conn = await get_create_connection()
    values = await conn.fetch(f"SELECT question_text FROM bot_questionsemotions")
    question_texts = [row['question_text'] for row in values]
    return question_texts


async def load_allpdf_emotions_answers(user_id: int) -> list:
    conn = await get_create_connection()
    value = await conn.fetch(f"SELECT answers, date FROM bot_answersemotions WHERE user_id=$1;", user_id)
    return value


async def delete_allpdf_emotions_answers(user_id: int) -> None:
    conn = await get_create_connection()
    await conn.execute("DELETE FROM bot_answersemotions WHERE user_id=$1;", user_id)