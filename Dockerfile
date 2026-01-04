FROM python:3.11-slim
WORKDIR /app
COPY requirements/production.txt req.txt
RUN pip install -r req.txt
COPY . .
WORKDIR /app/src
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
