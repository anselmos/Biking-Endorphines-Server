requirements:
	pip install -r requirements.txt

pylint: requirements
	pylint --load-plugins pylint_django bikingendorphines/web --rcfile=.pylintrc 
	pylint --load-plugins pylint_django bikingendorphines/tests --rcfile=.pylintrc 
	pylint --load-plugins pylint_django bikingendorphines/bikingendorphines --rcfile=.pylintrc 

unittest_with_prepare: prepare_db unittest

unittest:
	cd bikingendorphines && python manage.py test

prepare_db: requirements
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

deploy_gh_pages: pyreverse generate_pyreverse
	bash deploy_gh_pages.sh
