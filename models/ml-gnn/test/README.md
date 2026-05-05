# Testing

- Update local pypi repository

```sh
pip wheel -rpython/requirements.txt -w /mnt/storage1/LAB/pypi
pip wheel -rtests/requirements-test.txt -w /mnt/storage1/LAB/pypi
```

## Build test

We want to build for several target platforms.

### Raspi Build

This is the main lab platform.

### Docker Build

### OpenBSD Build

This compatibility would be nice but not strictly necessary.

### Debian Build
