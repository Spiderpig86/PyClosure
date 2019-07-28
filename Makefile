PYTHON ?= python3

all: test
test:
    ${PYTHON} tests/test_basic.py
check:
    ${PYTHON} setup.py check --restructuredtext