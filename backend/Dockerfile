# 1. Берём официальный готовый образ Python
FROM python:3.10-slim

# 2. Создаем внутри контейнера рабочую папку /app
WORKDIR /app

# 3. Копируем файл со списком библиотек в контейнер
COPY requirements.txt .

# 4. Устанавливаем библиотеки (FastAPI и Uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем остальной код (файл main.py) в контейнер
COPY . .

# 6. Команда для запуска сервера при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
