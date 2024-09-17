install:
	pip install --upgrade pip && pip install -r Requirements.txt

test:
	python3 -m pytest -vv --nbval -cov=mylib -cov=main_file test_*.py *.ipynb