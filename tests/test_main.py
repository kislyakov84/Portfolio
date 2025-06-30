# tests/test_main.py

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project


@pytest.mark.asyncio
async def test_root_with_no_projects(client: AsyncClient):
    """
    Тестируем главную страницу, когда в БД нет проектов.
    БД гарантированно пуста благодаря фикстуре db_session.
    """
    response = await client.get("/")

    assert response.status_code == 200
    assert "Проекты в разработке!" in response.text
    assert "Тестовый проект" not in response.text


@pytest.mark.asyncio
async def test_root_with_projects(client: AsyncClient, db_session: AsyncSession):
    """
    Тестируем главную страницу, когда в БД есть проекты.
    Ожидаем увидеть карточки проектов.
    """
    test_project = Project(
        name="Тестовый проект",
        description="Это описание для теста.",
        url="http://test.com",
    )
    db_session.add(test_project)
    await db_session.commit()

    response = await client.get("/")

    assert response.status_code == 200
    assert "Тестовый проект" in response.text
    assert "Проекты в разработке!" not in response.text


@pytest.mark.asyncio
async def test_admin_page_displays_projects(
    client: AsyncClient, db_session: AsyncSession
):
    """
    Тестируем, что на странице /admin отображается список проектов.
    """
    # 1. Arrange: Создаем тестовый проект в БД
    test_project = Project(
        name="Проект для админки",
        description="Описание тестового проекта.",
        url="http://admin-test.com",
    )
    db_session.add(test_project)
    await db_session.commit()

    # 2. Act: Делаем запрос к новой странице админки
    response = await client.get("/admin")

    # 3. Assert: Проверяем результат
    assert response.status_code == 200
    assert "Управление проектами" in response.text
    assert "Проект для админки" in response.text
    assert "Редактировать" in response.text  # Проверим наличие кнопок


@pytest.mark.asyncio
async def test_delete_project(client: AsyncClient, db_session: AsyncSession):
    """
    Тестируем удаление проекта через DELETE-запрос.
    """
    # Arrange: Создаем проект для удаления
    project_to_delete = Project(name="Проект на удаление", description="...")
    db_session.add(project_to_delete)
    await db_session.commit()
    await db_session.refresh(project_to_delete)  # Получаем его id из БД
    project_id = project_to_delete.id

    # Act: Отправляем DELETE-запрос, как это сделал бы HTMX
    response = await client.delete(f"/admin/projects/{project_id}")

    # Assert: Проверяем, что эндпоинт отработал успешно
    assert response.status_code == 200
    assert response.text == ""  # Ожидаем пустой ответ

    # Assert: Проверяем, что проекта больше нет в БД
    query = select(Project).where(Project.id == project_id)
    result = await db_session.execute(query)
    assert result.scalar_one_or_none() is None
