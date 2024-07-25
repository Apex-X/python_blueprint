CURRENT_TIMESTAMP := $(shell date +%s)

################################################################################################
# 								  Development Tools
################################################################################################

migration:
	@read -p "Enter migration name: " migration_name; \
	file_name=$(CURRENT_TIMESTAMP)_$$migration_name; \
	touch migrations/$$file_name.up.sql; \
	touch migrations/$$file_name.down.sql


################################################################################################
# 							  Formatter and Linter Tools
################################################################################################

isort:
	- isort --skip-glob=.tox --reverse-sort --profile=black ./..

flake8:
	- flake8 --exclude='.tox','__init__.py','venv/','tests/' --extend-exclude='*_pb2*.py' --max-line-length=121  ./..

blue:
	- blue --extend-exclude='__init__.py','tests/' ./..

lint: isort blue flake8

################################################################################################
# 							Formatter and Linter Tools for CI
################################################################################################

isort-ci:
	- isort --skip-glob=.tox --reverse-sort --check-only --profile=black ./..

flake8-ci:
	- flake8 --exclude='.tox','__init__.py','venv/','tests/' \
		 --extend-exclude='*_pb2*.py' --max-line-length=121 --count ./..

blue-ci:
	- blue --check --diff --extend-exclude='__init__.py','tests/' ./..

lint-ci: isort-ci blue-ci flake8-ci
