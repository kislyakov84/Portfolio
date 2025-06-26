# Мой сайт-портфолио

Сайт-портфолио, созданный на стеке FastAPI + HTMX + Tailwind CSS.

## Стек технологий

- Backend: FastAPI
- Frontend: HTMX, Tailwind CSS
- Database: PostgreSQL
- Testing: Pytest
- Tooling: uv, Ruff, pre-commit, Docker

## Запуск проекта локально

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <your-repo-url>
    cd portfolio-project
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    uv venv
    source .venv/bin/activate  # На Linux/macOS/WSL
    # .venv\Scripts\Activate.ps1 на PowerShell
    ```

3.  **Установите зависимости:**
    ```bash
    uv pip install -e .[dev]
    ```

4.  **Запустите веб-сервер:**
    ```bash
    uvicorn src.app.main:app --reload
    ```
    Приложение будет доступно по адресу `http://127.0.0.1:8000`.