# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    film_id: int
    title: str
    description: Optional[str] = None
    genre: str


movies = [
    Movie(film_id=1, title="Movie Шляпа", description="Description 1", genre="Action"),
    Movie(film_id=2, title="Movie Перчатки", description="Description 2", genre="Comedy"),
    Movie(film_id=3, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(film_id=4, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(film_id=5, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(film_id=6, title="Movie Упырь", description="Description 4", genre="Drama"),
]


@app.get("/")
async def read_root():
    return movies


@app.get("/genre")
async def filter_genre(genre: str):
    genre_movies = []
    for m in movies:
        if m.genre == genre:
            genre_movies.append(m)
    return genre_movies


@app.post("/items/")
async def create_item(movie: Movie):
    movies.append(movie)
    return movie


if __name__ == "__main__":
    uvicorn.run("task2:app", port=8080)
