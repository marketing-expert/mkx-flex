VENV := env
BIN := $(VENV)/bin
SHELL := /bin/bash
MANAGE := python manage.py

include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: ga-env
ga-env: ## Make a new virtual environment
	python3 -m venv $(VENV)
	source $(BIN)/activate
	python3 -m pip install --upgrade pip

.PHONY: ga-install
ga-install: ## Make venv and install requerements
	$(BIN)/pip install --upgrade -r requirements.txt

.PHONY: venv
venv: ## Make a new virtual environment
	pip3 install pipenv
	pipenv shell

.PHONY: install
install: venv ## Install or update dependencies
	pipenv install

freeze: ## Pin current dependencies
	pipenv lock -r > requirements.txt

migrate: ## Make and run migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

.PHONY: test
test: ## Run tests
	$(MANAGE) test core --verbosity=0 --parallel --failfast

createsuperuser: ## Run the Django server
	$(MANAGE) createsuperuser --username="flex-visitors" --email="flavienhugs@pm.me"

collectstatic: ## Run collectstatic
	$(MANAGE) collectstatic --no-input

dumpdata: ## dump data 
	$(MANAGE) dumpdata --indent=4 --natural-foreign --natural-primary -e contenttypes --format=json max.souscriber > _backups_/max_souscriber_data.json
	$(MANAGE) dumpdata --indent=4 --natural-foreign --natural-primary -e contenttypes --format=json flex.visitor > _backups_/flex_visitor_data.json

loaddata: ## load data 
	$(MANAGE) loaddata __backups__/*.json
