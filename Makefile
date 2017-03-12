requirements:
	pip install -r requirements.txt
pylint: requirements
	pylint bikingendorphines --rcfile=.pylintrc
unittest: requirements
	python bikingendorphines/manage.py test
