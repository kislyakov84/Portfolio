# create_tables.py
import asyncio
import sys

from sqlalchemy.ext.asyncio import create_async_engine

from app.db.base_class import Base

# from app.db.session import async_engine # <-- Не будем импортировать глобальный engine

# --- Исправление политики asyncio для Windows ---
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# --- Конец исправления ---

# Строка подключения для запуска скриптов с хост-машины
LOCALHOST_DB_URL = (
    "postgresql+asyncpg://portfolio_user:portfolio_pass@localhost:5432/portfolio_db"
)

# Создаем engine специально для этого скрипта
local_async_engine = create_async_engine(LOCALHOST_DB_URL)


async def create_tables() -> None:
    """
    Асинхронная функция для создания таблиц в базе данных.
    """
    print("Создание таблиц...")
    async with (
        local_async_engine.begin() as conn
    ):  # <-- Используем наш локальный engine
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы успешно созданы.")
    await local_async_engine.dispose()  # <-- Не забываем его закрыть


if __name__ == "__main__":
    asyncio.run(create_tables())
