install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py
