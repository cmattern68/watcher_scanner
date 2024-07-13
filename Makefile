VENV	= . venv/bin/activate
ISORT	= isort src/
BLACK	= black
MYPY	= mypy

.PHONY: dev
dev:
	python3.11 -m venv venv
	$(VENV) && pip install .[tests,lint,docs] && \
	pre-commit migrate-config && pre-commit install && \
	pip freeze > requirements/requirements-lock.txt && \
	pip install -e .

.PHONY: run
run:
	$(VENV) && \
	python3 local.py

.PHONY: fmt
fmt:
	$(ISORT) src/
	$(BLACK) src/

.PHONY: linting
linting:
	$(ISORT) src/ --check-only -df
	$(BLACK) src/ --check
	pylint src/

.PHONY: test
test:
	pytest -svv tests/

.PHONY: coverage
coverage:
	pytest --cov=src/ tests/

.PHONY: coverage-report
coverage-report:
	pytest --cov-report=html:/var/www/watcher_scanner/ --cov=src/ tests/

.PHONY: type-checkings
type-checkings:
	$(MYPY) src/

.PHONY: cleanup
cleanup:
	rm -rf build/ *.whl dist/ *.egg-info .mypy_cache .pytest_cache htmlcov/ .coverage
	find . -name "__pycache__" -type d -exec rm -rf {} \;
