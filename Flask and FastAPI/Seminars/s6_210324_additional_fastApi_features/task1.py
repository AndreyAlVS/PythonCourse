# Разработать API для управления списком пользователей с
# использованием базы данных SQLite.
# Для этого создайте модель User со следующими полями:
# id: int (идентификатор пользователя, генерируется автоматически)
# username: str (имя пользователя)
# email: str (электронная почта пользователя)
# password: str (пароль пользователя)
# API должно поддерживать следующие операции:
# Получение списка всех пользователей: GET /users/
# Получение информации о конкретном пользователе: GET /users/{user_id}/
# Создание нового пользователя: POST /users/
# Обновление информации о пользователе: PUT /users/{user_id}/
# Удаление пользователя: DELETE /users/{user_id}/
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr
import uvicorn
from random import choices

DATABASE_URL = "sqlite:///less_6_users.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
...
# engine = sqlalchemy.create_engine(DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
)
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class User(BaseModel):
    username: str = Field(title="Username", max_length=32)
    email: str = Field(title="Email", max_length=128)
    password: str = Field(title="Password")


class User_with_ID(User):
    user_id: int = Field(title="ID")


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f"user{i}", email=f"mail{i}@mail.ru", password=f"123456_{i}")
        await database.execute(query)
    return {"message": f"{count} fake users create"}


# create
@app.post("/users/", response_model=User_with_ID)
async def create_user(user: User):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    # print(user.model_dump())
    return {**user.model_dump(), "user_id": last_record_id}


# @app.get("/users/", response_model=List[User_with_ID])
# async def read_users():
# query = users.select()
# return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User_with_ID)
async def get_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@app.get("/users/", response_model=List[User_with_ID])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


if __name__ == "__main__":
    uvicorn.run("Less_6_Task_1:app", host="127.0.0.1", port=8000)
