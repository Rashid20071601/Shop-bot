# Импорт библиотек
import aiosqlite


# Функция для подключения к базе данных
async def create_connection():
    conn = await aiosqlite.connect("shop.db")
    cursor = await conn.cursor()
    await cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем поддержку FOREIGN KEY
    return conn