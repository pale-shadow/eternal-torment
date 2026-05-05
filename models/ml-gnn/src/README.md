# Source files

* The `pyproject` files open with qtcreator
* Update local pypi repository

```sh
pip wheel -rpython/requirements.txt -w /mnt/storage1/LAB/pypi
pip wheel -rtests/requirements-test.txt -w /mnt/storage1/LAB/pypi
```
