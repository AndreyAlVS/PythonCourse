from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///database_l6.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         )
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# Создание пользователя в БД, create
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    # query = users.insert().values(name=user.name, email=user.email)
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# Чтение пользователей из БД, read
@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# Чтение одного пользователя из БД, read
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


# Обновление пользователя в БД, update
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удаление пользователя из БД, delete
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
