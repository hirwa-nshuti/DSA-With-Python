#! /usr/bin/bash -e

echo "Starting local tests"

echo "General testing"
python3 -m pytest ArraysAndPractice/tests.py

echo "Reformating with balck"

black *.py

echo "Performing lint check"

cd ArraysAndPractice
for file in binary_search_algo.py list.py find_missing_unsorted.py linear_search.py tests.py; 
do
    pylint $file
done
cd ..

echo "Tests finished"
