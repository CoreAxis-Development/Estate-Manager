FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && (python manage.py loaddata /app/data/database_checkpoint_2.json || true) && python manage.py runserver 0.0.0.0:8000"]