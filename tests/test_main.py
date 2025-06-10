import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app  # Импорт остается тем же

# Обрати внимание на этот тип, который мы будем использовать в тесте
AppClient = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


@pytest.mark.asyncio
async def test_root_health_check():
    """
    Тестируем, что главная страница ("/") отвечает кодом 200
    и возвращает правильное сообщение.
    """
    async with AppClient as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
