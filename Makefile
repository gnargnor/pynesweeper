run: pip test

verbose: pip testv

pip:
	pip install . --upgrade

test: pip
	pytest ./test

testv: pip
	pytest ./test -vvv