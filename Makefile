requirements:
	pip install -r requirements.txt
pylint: requirements
	pylint bikingendorphines --rcfile=.pylintrc
unittest: requirements
	python bikingendorphines/manage.py test

prepare_db: requirements
	python bikingendorphines/manage.py makemigrations
	python bikingendorphines/manage.py migrate

runserver: prepare_db
	python bikingendorphines/manage.py runserver 0.0.0.0:8000
