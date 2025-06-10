# tests/test_main.py

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app

# Клиент остается прежним, он универсален
AppClient = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


@pytest.mark.asyncio
async def test_root_renders_html():
    """
    Тестируем, что главная страница ("/") возвращает HTML
    и содержит ожидаемый заголовок.
    """
    async with AppClient as client:
        response = await client.get("/")

    # 1. Проверяем, что ответ успешный
    assert response.status_code == 200

    # 2. Проверяем, что Content-Type правильный (HTML)
    assert "text/html" in response.headers["content-type"]

    # 3. Проверяем, что в полученном HTML есть наш заголовок
    assert "<title>Главная | Моё портфолио</title>" in response.text
    assert (
        '<h1 class="text-4xl font-bold">Привет! Я — твой будущий сайт-портфолио.</h1>'
        in response.text
    )
