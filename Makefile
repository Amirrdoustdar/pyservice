help:
	@echo "dev test lint run migrate"

dev:
	pip install -r requirements/development.txt -r requirements/testing.txt

test:
	cd src && python -m pytest ../tests -v

lint:
	ruff check src/

run:
	python manage.py runserver

migrate:
	python manage.py migrate
