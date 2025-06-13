# src/app/db/session.py
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings

# Создаем асинхронный "движок" для подключения к БД.
# echo=True полезно для отладки, т.к. выводит все SQL-запросы в консоль.
# В продакшене его лучше отключить.
async_engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Создаем фабрику асинхронных сессий.
# expire_on_commit=False предотвращает истечение срока действия объектов
# после коммита, что полезно в FastAPI.
async_session_factory = async_sessionmaker(bind=async_engine, expire_on_commit=False)
