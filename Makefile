run: pip test
	
pip:
	pip install . --upgrade

test: pip
	pytest ./test
