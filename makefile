# Makefile

.PHONY: install lint test run

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install flake8 pytest

lint:
	flake8 .

test:
	pytest -v

run:
	python random_hash.py
