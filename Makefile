install:
	pip install --upgrade pip && pip install -r Requirements.txt

lint:
	ruff check *.py