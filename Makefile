.PHONY: help install dev test lint serve docker docker-run ci clean

help:
	@echo "RestoPoS - Restaurant Point of Sale"
	@echo ""
	@echo "Usage:"
	@echo "  make install    Install dependencies"
	@echo "  make dev        Run development server"
	@echo "  make test       Run tests"
	@echo "  make lint       Run linter"
	@echo "  make serve      Run production server"
	@echo "  make docker     Build Docker image"
	@echo "  make docker-run Run Docker container"
	@echo "  make ci         Run CI checks (lint + test + docker)"
	@echo "  make clean      Clean up generated files"

install:
	pip install -r requirements.txt

dev:
	python app.py

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/

serve:
	gunicorn "app:create_app()" --bind 0.0.0.0:5000 --workers 2

docker:
	docker build -t resto-pos .

docker-run:
	docker run -p 5000:5000 resto-pos

ci: lint test docker
	@echo "CI checks passed!"

clean:
	rm -rf __pycache__ .pytest_cache htmlcov .coverage *.db
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
