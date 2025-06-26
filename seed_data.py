# seed_data.py
import asyncio
import sys  # <-- Добавили импорт

from app.db.session import async_session_factory
from app.models.project import Project

# --- НАЧАЛО ИСПРАВЛЕНИЯ ДЛЯ WINDOWS ---
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# --- КОНЕЦ ИСПРАВЛЕНИЯ ДЛЯ WINDOWS ---


async def seed_data() -> None:
    """
    Заполняет базу данных начальными данными.
    """
    print("Добавление начальных данных...")
    async with async_session_factory() as session:
        result = await session.execute("SELECT COUNT(id) FROM projects")
        if result.scalar_one() > 0:
            print("Данные уже существуют. Пропускаем.")
            return

        project1 = Project(
            name="Мой первый проект",
            description="Это описание моего первого крутого проекта на FastAPI.",
            url="https://github.com/kislyakov84/Portfolio",
        )
        project2 = Project(
            name="Супер Секретный Проект",
            description="Проект, который изменит мир. Скоро здесь будет ссылка.",
            url=None,
        )
        project3 = Project(
            name="Сайт-портфолио",
            description="Этот самый сайт. Мета-проект!",
            url="https://github.com/kislyakov84/Portfolio",
        )

        session.add_all([project1, project2, project3])
        await session.commit()
        print("Начальные данные успешно добавлены.")


if __name__ == "__main__":
    asyncio.run(seed_data())
