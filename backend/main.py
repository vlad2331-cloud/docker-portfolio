import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем нашему сайту (фронтенду) делать запросы к этому серверу
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Список цитат для рекрутеров
QUOTES = [
    "Ошибки — это знаки того, что вы пытаетесь. Продолжайте учиться!",
    "Каждый великий разработчик начинал с обычного print('Hello World').",
    "DevOps — это не просто инструменты, это культура автоматизации.",
    "Контейнеризация — это просто, если разбираться шаг за шагом!",
    "Вы нашли отличного джуна! Напишите Владу прямо сейчас."
]

@app.get("/api/quote")
def get_random_quote():
    # Выбираем случайную цитату из списка и возвращаем её
    return {"quote": random.choice(QUOTES)}
