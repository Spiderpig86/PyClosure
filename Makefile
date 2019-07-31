PYTHON ?= python3

all: build

build:
    ${PYTHON} setup.py sdist bdist_wheel

test:
    ${PYTHON} tests/test_basic.py

check:
    ${PYTHON} setup.py check --restructuredtext
