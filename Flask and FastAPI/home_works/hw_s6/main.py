# Создать веб-приложение на FastAPI, которое будет предоставлять API для
# работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения
# пользователей.
from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import sqlite3

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    birthdate: date = Field(..., description="Date of birth in the format 'YYYY-MM-DD'")
    email: EmailStr = Field(..., description="Email in the format 'str@str.str'")
    address: str


conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              birthdate TEXT,
              email TEXT,
              address TEXT)''')
conn.commit()


@app.post("/users")
async def create_user(user: User):
    c.execute('''INSERT INTO users (name, surname, birthdate, email, address)
                 VALUES (?, ?, ?, ?, ?)''',
              (user.name, user.surname, user.birthdate, user.email, user.address))
    conn.commit()
    return {"message": "User created successfully"}


@app.get("/users")
async def get_all_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    result = []
    for user in users:
        user_dict = {"id": user[0],
                     "name": user[1],
                     "surname": user[2],
                     "birthdate": user[3],
                     "email": user[4],
                     "address": user[5]}
        result.append(user_dict)

    return result


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()

    if user:
        user_dict = {"id": user[0],
                     "name": user[1],
                     "surname": user[2],
                     "birthdate": user[3],
                     "email": user[4],
                     "address": user[5]}
        return user_dict
    else:
        return {"message": "User not found"}


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    c.execute('''UPDATE users SET name=?, surname=?, birthdate=?, email=?, address=?
                 WHERE id=?''',
              (user.name, user.surname, user.birthdate, user.email, user.address, user_id))
    conn.commit()
    return {"message": "User updated successfully"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    return {"message": "User deleted successfully"}
