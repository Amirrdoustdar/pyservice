# PyService

## Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
python manage.py migrate
python manage.py runserver

## Endpoints
- /api/v1/health/
- /api/docs/
