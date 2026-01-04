FROM python:3.11-slim

WORKDIR /app

# Copy all requirements
COPY requirements/ requirements/

# Install dependencies
RUN pip install --no-cache-dir -r requirements/production.txt

# Copy project
COPY . .

WORKDIR /app/src

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
