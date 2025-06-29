# src/app/schemas/project_schema.py
from pydantic import BaseModel, HttpUrl


class ProjectCreate(BaseModel):
    """
    Схема для создания нового проекта.
    """

    name: str
    description: str
    url: HttpUrl | None = None  # Используем HttpUrl для автоматической валидации URL


class ProjectRead(ProjectCreate):
    """
    Схема для чтения проекта (включая id).
    """

    id: int

    # Эта конфигурация позволяет Pydantic читать данные
    # не только из dict, но и из атрибутов объектов (как у моделей SQLAlchemy).
    class Config:
        from_attributes = True
