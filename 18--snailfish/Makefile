.PHONY: run test example

SHELL=/bin/bash

run:
	@echo With my input;
	@python3 a.py
	@python3 b.py

example:
	@echo With example input:
	@python3 a.py example
	@python3 b.py example

test:
	python3 -m doctest a.py
	python3 -m doctest b.py
	python3 -m doctest more_tests.txt
