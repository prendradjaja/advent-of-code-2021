# Not really a "real" Makefile. This isn't for any sort of compilation step.
# It just makes it easy for me to run my code (I have a shortcut for "make" in
# my text editor.)
#
# Piping to tee >(tail -n1 |pbcopy) allows me to simultaneously
# - View the full output
# - Copy just the last line into my clipboard

.PHONY: run test copy-last example

SHELL=/bin/bash

run:
	@pyx s.py

test:
	clear
	mkdir -p dist
	pyxcompile s.py > dist/s.py
	python3 -m doctest dist/s.py

copy-last:
	pyx s.py | tee >(tail -n1 | pbcopy)

example:
	@pyx s.py example
