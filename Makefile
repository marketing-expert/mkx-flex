MANAGE := python manage.py

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: shell
shell: ## Make a new virtual environment
	pipenv shell

.PHONY: install
install: shell ## Install or update dependencies
	pipenv install

freeze: ## Pin current dependencies
	pipenv lock -r > requirements.txt

.PHONY: install-dep
install-dep: ## Make venv and install requerements
	pip3 install --upgrade -r requirements.txt

migrate: ## Make migrations and run migrate
	$(MANAGE) makemigrations
	$(MANAGE) migrate

.PHONY: test
test: ## Run test
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
