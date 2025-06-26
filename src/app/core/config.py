# src/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс для хранения настроек приложения.
    Pydantic автоматически читает переменные из .env файла.
    """

    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")


# --- БОЕВОЙ КОД ---
# Ввиду аномалий окружения на Windows, мы жестко задаем DATABASE_URL,
# чтобы гарантировать правильное подключение к Docker.
# Это решение имеет наивысший приоритет и перекрывает любые внешние переменные.
# settings = Settings(
#    DATABASE_URL="postgresql+asyncpg://portfolio_user:portfolio_pass@host.docker.internal:5432/portfolio_db"
# )
settings = Settings()
# УБЕДИСЬ, ЧТО ЭТА СТРОКА ЕСТЬ И ФАЙЛ СОХРАНЕН:
# rint(f"!!! ИСПОЛЬЗУЕТСЯ DATABASE_URL: {settings.DATABASE_URL} !!!")
