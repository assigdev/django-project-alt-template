# Makefile for the django project.
#

DATE = $(shell date +%Y-%m-%d)
path ?= .
PACKAGE_NAME = {{ project_name }}
SHELL = bash
PORT = 5010
WEB = backend
DB = db
build = 0


default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make dev        up project for development'
	@echo '    make dev_easy   up project without container for development'
	@echo '    make prod       up project in production'
	@echo '    make dump       dump db from postgres'
	@echo '    make restore    restore db from postgres'
	@echo '    make configure  configure project for first start'
	@echo '    make update     update project for production'
	@echo


dev:
ifeq ($(build), 1)
	docker-compose up --build
else
	docker-compose up
endif


dev_light:
ifeq ($(build), 1)
	pip install pipenv && pipenv install --dev
	pipenv run python manage.py migrate
	pipenv run python manage.py loaddata fixtures.json
	pipenv run python manage.py createsuperuser
endif
	pipenv run python manage.py runserver 0.0.0.0:$(PORT)


prod:
ifeq ($(build), 1)
	docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up --build
else
	docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up
endif


configure:
	docker-compose exec backend python manage.py migrate
	docker-compose exec backend python manage.py collectstatic
	docker-compose exec backend python manage.py createsuperuser


update:
	docker-compose exec backend python manage.py migrate
	docker-compose exec backend python manage.py collectstatic


load_fixtures:
	docker-compose exec backend python manage.py loaddata fixtures.json


dump: ## dump db, usage 'make dump path=/path/to/dumps'
	docker-compose exec --user postgres $(DB) pg_dumpall --clean | gzip > $(path)/project-$(DATE).sql.gz


restore: ## restore db from dump file, usage 'make restore dump=dump.sql.gz'
	docker-compose stop $(WEB)
	gunzip -c $(dump) | docker exec -i --user postgres `docker-compose ps -q $(DB)` psql
	docker-compose start $(WEB)


.PHONY: default dev prod configure update dev_light dump restore