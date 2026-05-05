# Eternal Torment Repository Summary

Repository: pale-shadow/eternal-torment
Purpose: A sandbox repository dedicated to coding practice, experimentation, and continuous learning.
Context: Part of the pale-shadow GitHub organization, which hosts repositories for CTF tools, bot code, and #badgelife plans for security conference badge hardware. The eternal-torment repository serves as a chaotic but functional testing ground for various programming languages, build systems, and technical experiments.

## Repository Reorganization

The repository has recently undergone a major structural reorganization. All primary source code, previously scattered at the root level, has been consolidated into a dedicated src/ directory. This groups the code logically by project, platform, or programming challenge.

## Project Structure & Focus Areas

1. Low-Level & Assembly (src/ass/, src/funk.s)

AArch64 Assembly: Practicing ARM64 assembly via hello.s, fileio.s, gpiomem.s, and shift.s. This module focuses heavily on system calls and memory manipulation.

Build Automation: Contains its own setup.sh and GNU Autotools configurations (configure.ac, Makefile.am) for assembling binaries natively.

2. C Programming & OpenGL (src/cube1/, src/freeglut/, src/SpinningCube/)

Graphics Rendering: Multiple subdirectories dedicated to graphics rendering practice using OpenGL, GLUT/FreeGLUT, and X11, accompanied by standard Makefiles.

General C: Includes standalone C files like main.c and cryptographic implementations in C.

3. Algorithm Challenges & Math

HackerRank (src/hackerrank/): Python scripts for HackerRank challenges (e.g., string capitalization, exception handling).

Project Euler (src/projecteuler.net/): Solutions to various Project Euler mathematical challenges implemented in Python (Problems 1, 2, 3, 5, and 31).

Calculations & Vectors (src/calc-pi/, src/vectors/): Python scripts dedicated to calculating Pi and performing vector math (dot products, scalar multiplication, vector creation).

4. Cryptography (src/trithemius/)

Implementations of the Trithemius cipher in multiple languages, including both C (trithemius.c) and Python (trithemius.py).

5. Machine Learning & DevOps (src/tensorflow/, src/betty-lab/)

TensorFlow: Contains scripts (tf.py), dependency lists (tensorflow2.yml, requirements.txt), and containerization infrastructure (including a Dockerfile and a Kubernetes tf-pod.yaml).

Betty Lab: A Python-based project environment.

## Build System Integration

The top-level src/ directory and its subdirectories rely heavily on GNU Autotools and standard Makefiles. Root files such as Makefile.am and Makefile.in indicate that a unified build pipeline is used to manage and compile the various C and Assembly projects simultaneously.

## License and Maintainers

Maintainers: devsecfranklin (Franklin D.)

License: Apache-2.0 License

## Getting Started

To explore the source code:

Clone the repository and navigate to the src/ directory.

For assembly projects, navigate to src/ass/ and run ./setup.sh (Note: requires an ARM64 system or emulator).

For Python projects, verify dependencies in the respective requirements.txt files before execution.