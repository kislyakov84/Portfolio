# src/app/repositories/project_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project


async def get_projects(db: AsyncSession) -> list[Project]:
    """
    Получает все проекты из базы данных
    """
    query = select(Project).order_by(Project.id)
    result = await db.execute(query)
    return list(result.scalars().all())


async def get_project_by_id(db: AsyncSession, project_id: int) -> Project | None:
    """
    Получает один проект по его ID.
    """
    # db.get() - это самый эффективный способ получить объект по primary key.
    return await db.get(Project, project_id)
