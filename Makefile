requirements:
	pip install -r requirements.txt
pylint: requirements
	pylint --load-plugins pylint_django bikingendorphines/web --rcfile=.pylintrc 
	pylint --load-plugins pylint_django bikingendorphines/bikingendorphines --rcfile=.pylintrc 
unittest: prepare_db
	python bikingendorphines/manage.py test
	python bikingendorphines/manage.py test web

prepare_db: requirements
	python bikingendorphines/manage.py makemigrations
	python bikingendorphines/manage.py migrate

runserver: prepare_db
	python bikingendorphines/manage.py runserver 0.0.0.0:8000

pyreverse: requirements
	pyreverse -AS -o png --project=Biking-Endorphines-Web bikingendorphines/web/

gh_pages: pyreverse
	ls -alth classes_Biking-Endorphines-Web.png
	ls -alth packages_Biking-Endorphines-Web.png
