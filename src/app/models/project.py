# src/app/models/project.py
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Project(Base):
    """
    Модель для проекта в портфолио.
    """

    __tablename__ = "projects"

    name: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str | None] = mapped_column(String(255), nullable=True)
