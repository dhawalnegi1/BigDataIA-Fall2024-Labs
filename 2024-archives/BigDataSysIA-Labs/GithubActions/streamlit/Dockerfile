FROM python:3.10-slim

WORKDIR /app

# Copy Poetry config and lock file from root
COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && poetry install --no-root

COPY ./streamlit/ ./ 

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
