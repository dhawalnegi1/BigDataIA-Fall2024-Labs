FROM python:3.10-slim

WORKDIR /app

# Copy Poetry configuration from the root
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install --no-cache-dir poetry && poetry install --no-root --no-dev

# Copy the FastAPI application files
COPY ./backend/ ./ 
# Ensure the correct directory is referenced

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
