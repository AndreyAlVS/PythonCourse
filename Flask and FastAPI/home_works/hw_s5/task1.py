# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
# Реализуйте валидацию данных запроса и ответа.
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.post("/add_user")
async def add_user(request: Request, user: User = Form(...)):
    users.append(user)
    return await templates.TemplateResponse("home.html", {"request": request, "users": users})


@app.put("/update_user/{id}")
async def update_user(request: Request, id: int, user: User = Form(...)):
    for i, u in enumerate(users):
        if u.id == id:
            users[i] = user
            break
    return await templates.TemplateResponse("home.html", {"request": request, "users": users})


@app.delete("/delete_user/{id}")
async def delete_user(request: Request, id: int):
    for i, u in enumerate(users):
        if u.id == id:
            del users[i]
            break
    return await templates.TemplateResponse("home.html", {"request": request, "users": users})


@app.get("/")
async def home(request: Request):
    return await templates.TemplateResponse("home.html", {"request": request, "users": users})


if __name__ == "__main__":
    uvicorn.run("task1:app", port=8080)
