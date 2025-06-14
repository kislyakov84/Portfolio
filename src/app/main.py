# src/app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # <-- Импортируем StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Portfolio App")

# Монтируем директорию static для раздачи статических файлов (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="src/app/static"), name="static")

# Указываем FastAPI, где лежат шаблоны
templates = Jinja2Templates(directory="src/app/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Отображает главную страницу портфолио.
    """
    # request: Request - обязательный параметр для рендеринга шаблона
    # "index.html" - имя файла шаблона
    # {"request": request} - контекст, который передается в шаблон
    return templates.TemplateResponse(
        name="index.html", context={"request": request, "title": "Главная"}
    )
