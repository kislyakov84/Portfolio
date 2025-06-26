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
