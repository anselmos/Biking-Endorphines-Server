requirements:
	pipenv install

pylint_all: requirements pylint

pylint:
	pipenv run pylint --load-plugins pylint_django bikingendorphines/web --rcfile=.pylintrc 
	pipenv run pylint --load-plugins pylint_django bikingendorphines/api --rcfile=.pylintrc 
	pipenv run pylint --load-plugins pylint_django bikingendorphines/bikingendorphines --rcfile=.pylintrc 

unittest_all: prepare_db unittest

unittest:
	cd bikingendorphines && pipenv run python3 manage.py test

unittest_debug:
	cd bikingendorphines && pipenv run python3 manage.py test -v 2

prepare_db_all: requirements prepare

prepare_db:
	pipenv run python3 bikingendorphines/manage.py makemigrations
	pipenv run python3 bikingendorphines/manage.py migrate

runserver: prepare_db
	pipenv run python3 bikingendorphines/manage.py runserver 0.0.0.0:8000

pyreverse:
	rm -rf generated_pyreverse
	mkdir -p generated_pyreverse
	pipenv run pyreverse -AS -o png --project=Biking-Endorphines-Web bikingendorphines/web/
	mv *.png generated_pyreverse/

generate_pyreverse:
	bash generate_pyreverse_markdown.sh

deploy_gh_pages_all: pyreverse generate_pyreverse deploy_gh_pages

deploy_gh_pages:
	bash deploy_gh_pages.sh

setup_pipenv:
	pipenv --python 3.6
