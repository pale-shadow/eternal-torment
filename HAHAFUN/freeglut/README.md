# freeglut

* [Main project page](https://freeglut.sourceforge.net/)
* [Github page for the project](https://github.com/freeglut/freeglut)
* [Draw a rotating cube](https://rosettacode.org/wiki/Draw_a_rotating_cube#C)

## OpenBSD Build

```sh
doas pkg_add cmake
cd /usr/ports/graphics/freeglut && doas make
gcc freeglut-cube.c -o fg -lGL -lGLU -lglut
```
