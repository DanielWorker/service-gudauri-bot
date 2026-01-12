FROM python:3.12-slim

# Не буферизуем stdout → логи сразу видны
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Системные зависимости (psycopg2, ffmpeg если нужен и т.д.)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# ВАЖНО: чтобы src был доступен как пакет
ENV PYTHONPATH=/app

# Создаём директории под логи и сессии (на случай пустых volume)
RUN mkdir -p logs sessions

# Запуск бота
CMD ["python", "-m", "src.main"]