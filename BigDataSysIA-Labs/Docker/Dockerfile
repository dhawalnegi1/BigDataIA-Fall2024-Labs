# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the application code
COPY docker/ /app/

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app using Poetry
CMD ["poetry", "run", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
