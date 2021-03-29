install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C streamlit-ui.py app.py mylib/*.py


test: 
	python -m pytest -vv --cov=mylib --cov=app_test app_test.py