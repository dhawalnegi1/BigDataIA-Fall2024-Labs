FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY ./fastapi_demo /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
