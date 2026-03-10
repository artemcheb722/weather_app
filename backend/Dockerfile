FROM python:3.12-slim

WORKDIR /app

# Устанавливаем системные зависимости (если нужны)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем только файлы с зависимостями (для кэширования)
COPY pyproject.toml poetry.lock* ./

# Устанавливаем poetry и зависимости
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем весь проект
COPY . .

# Запускаем
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]