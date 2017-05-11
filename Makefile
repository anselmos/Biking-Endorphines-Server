requirements:
	pip install -r requirements.txt

pylint_all: requirements pylint

pylint:
	pylint bikingendorphines/web --rcfile=.pylintrc 
	pylint bikingendorphines/bikingendorphines --rcfile=.pylintrc 

unittest_all: prepare_db unittest

unittest:
	cd bikingendorphines && python manage.py test

prepare_db_all: requirements prepare

prepare_db:
	python bikingendorphines/manage.py makemigrations
	python bikingendorphines/manage.py migrate

runserver: prepare_db
	python bikingendorphines/manage.py runserver 0.0.0.0:8000

pyreverse: requirements
	rm -rf generated_pyreverse
	mkdir -p generated_pyreverse
	pyreverse -AS -o png --project=Biking-Endorphines-Web bikingendorphines/web/
	mv *.png generated_pyreverse/

generate_pyreverse:
	bash generate_pyreverse_markdown.sh

deploy_gh_pages_all: pyreverse generate_pyreverse deploy_gh_pages

deploy_gh_pages:
	bash deploy_gh_pages.sh
