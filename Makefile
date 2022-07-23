install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-aws:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	for dir in binary_search_algo.py list.py find_missing_unsorted.py LinearSearch.py tests.py ; do \
    pylint ArraysAndPractice/$$dir ; \
	done

test:
	python -m pytest ArraysAndPractice/tests.py