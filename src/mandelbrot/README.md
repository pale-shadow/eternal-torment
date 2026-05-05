# mandelbrot

`gcc fractal.c -o fractal -lm`
`gcc julia-cube.c -lGL -lGLU -lglut -lm -o julia-cube`
`gcc julia-reshape.c -lGL -lGLU -lglut -lm -o jr`

```sh
gcc julia.ppm.c -o julia -lm
./julia
convert julia.ppm julia.png 
```

## Beautiful Fractal Constants for 2026

Try swapping the c value in your code with these famous patterns:
| --- | --- | --- |
| Pattern Name | Constant () | Visual Style |
| The Cauliflower	| c = 0.25 + 0i | Very organic, rounded "blooms." | 
| San Marco | c = -0.75 + 0i | Looks like the floor plan of a cathedral. |
| Douady's Rabbit | c = -0.123 + 0.745i | Three-way symmetry with "ear" shapes. |
| Spirals | c = -0.8 + 0.156i | Tight, lightning-bolt-like spirals. |