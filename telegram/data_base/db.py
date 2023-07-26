import asyncpg

from telegram.create_bot import DATABASE_URL

connection = None

async def get_create_connection() -> asyncpg.Connection:
    global connection
    if connection is None:
        connection = await asyncpg.connect(dsn=DATABASE_URL)
    return connection

