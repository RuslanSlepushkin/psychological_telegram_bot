import json

from datetime import datetime
from telegram.data_base.db import get_create_connection


async def get_question_fallingarrow(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT question_text FROM bot_questionsfallingarrow WHERE id = $1", num)
    return value


async def get_text_fallingarrow(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT text FROM bot_questionsfallingarrow WHERE id = $1", num)
    return value


async def down_fallingarrow(user_id: int, data: dict) -> None:
        conn = await get_create_connection()
        time = datetime.now().replace(second=0, microsecond=0)
        json_data = json.dumps(data)
        await conn.execute("INSERT INTO bot_answersfallingarrow (user_id, answers, date) VALUES ($1, $2, $3)",
                           user_id, json_data, time)


async def load_pdf_fallingarrow_answers(user_id: int) -> dict:
    conn = await get_create_connection()
    value = await conn.fetchval(f"SELECT answers FROM bot_answersfallingarrow WHERE user_id = "
                                f"{user_id} ORDER BY id DESC LIMIT 1;")
    return value


async def load_pdf_fallingarrow_questions() -> list:
    conn = await get_create_connection()
    values = await conn.fetch(f"SELECT question_text FROM bot_questionsfallingarrow")
    question_texts = [row['question_text'] for row in values]
    return question_texts


async def delete_allpdf_fallingarrow_answers(user_id: int) -> None:
    conn = await get_create_connection()
    await conn.execute("DELETE FROM bot_answersfallingarrow WHERE user_id=$1;", user_id)
    await conn.execute("DELETE FROM bot_answersabcmodel WHERE user_id=$1;", user_id)
    await conn.execute("DELETE FROM bot_answersworklist WHERE user_id=$1;", user_id)