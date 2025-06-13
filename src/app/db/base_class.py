# src/app/db/base_class.py
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей SQLAlchemy.
    Включает в себя общие поля, такие как id.
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
