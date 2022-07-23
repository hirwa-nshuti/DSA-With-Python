install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-aws:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint $(git ls-files '*.py')

test:
	python -m pytest ArraysAndPractice/tests.py