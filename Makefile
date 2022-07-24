install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black $(git ls-files '*.py')

lint:
	for dir in binary_search_algo.py list.py find_missing_unsorted.py LinearSearch.py tests.py ; do \
    pylint ArraysAndPractice/$$dir ; \
	done
flake:
	flake8 $(git ls-files '*.py')	
test:
	python -m pytest ArraysAndPractice/tests.py