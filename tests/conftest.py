# tests/conftest.py

from pathlib import Path
from typing import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.db.base_class import Base
from app.main import app, get_db

# --- Путь к файлу тестовой БД ---
TEST_DB_PATH = Path("test.db")

# --- Настройки тестовой БД ---
TEST_DATABASE_URL = f"sqlite+aiosqlite:///{TEST_DB_PATH}"

# Создаем Engine один раз для всего модуля
test_engine = create_async_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Создаем Фабрику сессий один раз для всего модуля
TestSessionFactory = async_sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Главная фикстура: создает таблицы, отдает сессию, удаляет таблицы.
    """
    # Создаем таблицы ПЕРЕД каждым тестом
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Отдаем сессию в тест
    async with TestSessionFactory() as session:
        yield session

    # Удаляем таблицы ПОСЛЕ каждого теста
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """
    Фикстура для HTTP-клиента, которая переопределяет зависимость `get_db`.
    """

    # Функция, которую FastAPI будет вызывать вместо `get_db`
    async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        yield c

    del app.dependency_overrides[get_db]
