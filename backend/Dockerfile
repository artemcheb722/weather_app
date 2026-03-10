FROM python:3.12-slim

WORKDIR /app

# установить poetry
RUN pip install poetry

# отключить виртуальное окружение poetry

# копируем зависимости
COPY pyproject.toml poetry.lock* ./

# установить зависимости
RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

# копируем код
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]