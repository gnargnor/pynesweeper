run: pip test
	
pip:
	pip install .

test: pip
	pytest ./test
