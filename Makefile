package = .

tests:
	python -m unittest discover -s $(package)
