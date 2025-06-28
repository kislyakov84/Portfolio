# src/app/main.py

from collections.abc import AsyncGenerator

import sqlalchemy.exc  # Импортируем исключения sqlalchemy
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Импорты из нашего приложения
from app.db.base_class import Base
from app.db.session import async_engine, async_session_factory
from app.models.project import Project
from app.repositories import project_repository

app = FastAPI(title="Portfolio App")

app.mount("/static", StaticFiles(directory="src/app/static"), name="static")

templates = Jinja2Templates(directory="src/app/templates")


# Зависимость для получения сессии БД
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Зависимость для получения асинхронной сессии базы данных.
    """
    async with async_session_factory() as session:
        yield session


@app.on_event("startup")
async def on_startup():
    """
    Создает таблицы в базе данных при старте приложения и
    добавляет тестовые данные, если таблица пуста.
    """
    async with async_engine.begin() as conn:
        # Для разработки можно использовать drop_all, но в проде это опасно
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # Добавляем демо-данные, если проектов еще нет
    async with async_session_factory() as session:
        query = select(Project).limit(1)
        result = await session.execute(query)
        if not result.scalars().first():
            demo_projects = [
                Project(
                    name="Этот сайт-портфолио",
                    description=(
                        "Сайт, который вы сейчас просматриваете. "
                        "Создан на FastAPI, HTMX и TailwindCSS."
                    ),
                    url="#",
                ),
                Project(
                    name="Система управления задачами",
                    description=(
                        "REST API для простого таск-менеджера с "
                        "аутентификацией пользователей."
                    ),
                    url="https://github.com",
                ),
                Project(
                    name="Анализатор текста",
                    description=(
                        "Инструмент, который анализирует текст и выдает "
                        "статистику по словам и символам."
                    ),
                    url=None,
                ),
            ]
            session.add_all(demo_projects)
            await session.commit()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: AsyncSession = Depends(get_db)):
    """
    Отображает главную страницу портфолио со списком проектов.
    """
    try:
        projects = await project_repository.get_projects(db)
        return templates.TemplateResponse(
            request,  # <--- Проверяем здесь
            name="index.html",
            context={"projects": projects, "title": "Главная"},
        )
    except sqlalchemy.exc.OperationalError:
        # Это временная "заглушка" на случай, если БД недоступна.
        return templates.TemplateResponse(
            request,  # <--- И здесь
            name="index.html",
            context={
                "projects": [],
                "error": "Не удалось подключиться к базе данных.",
                "title": "Ошибка",
            },
        )
