# src/app/main.py

from fastapi import FastAPI

# Создаем экземпляр FastAPI
app = FastAPI(title="Portfolio API")


@app.get("/")
async def read_root():
    """
    Главная страница / Health Check.
    """
    return {"message": "Hello, World!"}
