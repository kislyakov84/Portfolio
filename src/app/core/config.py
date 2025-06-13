# src/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс для хранения настроек приложения.
    Pydantic автоматически читает переменные из .env файла.
    """

    DATABASE_URL: str

    # Указываем Pydantic, что нужно прочитать переменные из файла .env
    model_config = SettingsConfigDict(env_file=".env")


# Создаем экземпляр настроек, который будет использоваться в приложении
settings = Settings()
