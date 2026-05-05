# mandelbrot

While the Mandelbrot set is the "map" of all possible Julia sets, each
individual Julia set is determined by that constant $c$. Small tweaks
to those coordinates completely transform the topology of the resulting
image.

```sh
gcc fractal.c -o fractal -lm
gcc julia-cube.c -lGL -lGLU -lglut -lm -o julia-cube
gcc julia-reshape.c -lGL -lGLU -lglut -lm -o jr
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

## Julia Sets

A Julia set is a type of fractal defined by iterating the complex
polynomial formula $z_{n+1} = z_n^2 + c$, where $z$ is a starting point on the
complex plane and $c$ is a constant complex number. Points that remain bounded
(do not diverge to infinity) under this iteration form the set, producing highly
intricate, self-similar, and connected or disconnected shapes depending on the
value of $c$. [1, 2, 3, 4, 5]  

### Key Aspects and Usage Examples 

- Relation to Mandelbrot Set: If the constant $c$ is chosen from inside the Mandelbrot set, the Julia set is connected; if $c$ is outside, it is a disconnected "Cantor dust" or fractal dust. 
- Visual Representation: Julia sets are visualized by coloring points based on how quickly their orbits diverge to infinity (or if they stay within a boundary). 
- Types of Julia Sets: Examples include the "Douady's rabbit," "San Marco fractal," and "dendrite" shapes, often used to showcase complex dynamical systems. 
- Mathematical Foundation: They are the boundary between points that converge to infinity and those that converge to a stable attractor, discovered by Gaston Julia. [3, 4, 6, 7, 8, 9]  

### Synonyms and Related Terms 

- Filled Julia Set: The solid set of all points that do not escape to infinity, whereas the "Julia set" often refers strictly to the boundary of this set. 
- Fatou Set: The complement of the Julia set, consisting of points where behavior is stable, while the Julia set itself is the set of chaotic points. 
- Complex Dynamical System: The broader field of mathematics that studies the iteration of functions. [4, 5, 6, 10, 11]  

[1] https://www.youtube.com/watch?v=mg4bp7G0D3s
[2] https://www.karlsims.com/julia.html
[3] https://www.youtube.com/watch?v=AH1CGuMI61M
[4] https://www.cantorsparadise.com/the-julia-set-e03c29bed3d0
[5] https://e.math.cornell.edu/people/belk/dynamicalsystems/NotesJuliaMandelbrot.pdf
[6] https://www.youtube.com/watch?v=dctJ7ISkU-4
[7] https://paulbourke.net/fractals/juliaset/
[8] https://www.britannica.com/science/Julia-set
[9] https://occupymath.wordpress.com/2018/02/15/where-are-the-beautiful-julia-sets/
[10] https://en.wikipedia.org/wiki/Julia_set
[11] https://simple.wikipedia.org/wiki/Julia_set

