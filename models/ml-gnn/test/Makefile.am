
CLOCAL_AMFLAGS = -I config/m4 -I aclocal
ACLOCAL_AMFLAGS = -I config/m4 -I aclocal

.PHONY: test

test: ## run all test cases
	@$(PY39) -m venv _build
	( \
		source ../_build/bin/activate; \
		../_build/bin/python -m pip install --upgrade pip; \
		../_build/bin/python -m pip install tox; \
		../_build/bin/python -m pip install -rrequirements-test.txt; \
		../_build/bin/python -m pip install -rrequirements-security.txt; \
	)
