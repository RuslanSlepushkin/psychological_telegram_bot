import json

from datetime import datetime
from telegram.data_base.db import get_create_connection


async def get_question_abcmodel(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT question_text FROM bot_questionsabcmodel WHERE id = $1", num)
    return value


async def get_text_abcmodel(num: int) -> str:
    conn = await get_create_connection()
    value = await conn.fetchval("SELECT text FROM bot_questionsabcmodel WHERE id = $1", num)
    return value


async def down_abcmodel(user_id: int, data: dict) -> None:
        conn = await get_create_connection()
        time = datetime.now().replace(second=0, microsecond=0)
        json_data = json.dumps(data)
        await conn.execute("INSERT INTO bot_answersabcmodel (user_id, answers, date) VALUES ($1, $2, $3)",
                           user_id, json_data, time)


async def load_pdf_abcmodel_answers(user_id: int) -> dict:
    conn = await get_create_connection()
    value = await conn.fetchval(f"SELECT answers FROM bot_answersabcmodel WHERE user_id = "
                                f"{user_id} ORDER BY id DESC LIMIT 1;")
    return value


async def load_pdf_abc_questions() -> list:
    conn = await get_create_connection()
    values = await conn.fetch(f"SELECT question_text FROM bot_questionsabcmodel")
    question_texts = [row['question_text'] for row in values]
    return question_texts