CLOCAL_AMFLAGS = -I config/m4 -I aclocal
ACLOCAL_AMFLAGS = -I config/m4 -I aclocal

.PHONY: cluster docs paper presentation tests

clean:
	rm -rf _build *.egg-info
	find . -name '*.pyc' | xargs rm -rf
	find . -name '__pycache__' | xargs rm -rf
	for trash in _collect autom4te.cache config config.log _viz\
		config.status configure configure~ libtool Makefile Makefile.in po\
		cluster/Makefile cluster/Makefile.in docker/Makefile docker/Makefile.in _test; do \
			if [ -f $$trash ] || [ -d $$trash ]; then \
				echo "Removing $$trash" ;\
				rm -rf $$trash ;\
			fi ; \
	done

collect:
	@$(PY39) -m venv _collect
	( \
		. _collect/bin/activate; \
		_collect/bin/python -m pip install --no-index --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi tox; \
		_collect/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi --upgrade pip; \
		_collect/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi -r src/collection/requirements.txt; \
	)

test:
	@$(PY39) -m venv _test
	( \
		. _test/bin/activate; \
		_test/bin/python -m pip install --no-index --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi tox; \
		_test/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi --upgrade pip; \
		_test/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi -r test/requirements.txt; \
	)

visualize:
	@$(PY39) -m venv _viz
	( \
		. _viz/bin/activate; \
		_viz/bin/python -m pip install --no-index --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi tox; \
		_viz/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi --upgrade pip; \
		_viz/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi -r src/visualize/requirements.txt; \
	)