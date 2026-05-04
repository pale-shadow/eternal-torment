# Eternal Torment

A sandbox repository dedicated to coding practice, experimentation, and continuous learning.

## About This Repository

This repository serves as a chaotic but functional testing ground for various programming languages, build systems, and technical experiments. Because the primary goal of this repo is pure coding practice, the architecture and contents will frequently change, break, or be rewritten as new concepts are explored.

## Current Experiments

Recent updates focus on low-level programming and build automation:

* **AArch64 Assembly (`ass/`):** Practicing ARM64 assembly via `hello.s`, utilizing AArch64 `write(2)` system calls.
* **GNU Autotools:** Setting up dynamic build environments using `configure.ac` and `Makefile.am` to compile assembly code.
* **Automation & Scripting:** Basic environment setup and repository cleanup scripts (`setup.sh`, `cleanup.sh`).

## Getting Started

If you want to pull down the code and run the current assembly environment:

1.  **Clone the repository:**
    
    ```sh
    git clone [https://github.com/pale-shadow/eternal-torment.git](https://github.com/pale-shadow/eternal-torment.git)
    cd eternal-torment
    ```

2.  **Explore the code:**
    
    To inspect or modify the source files, use `vi`:
    
    ```bash
    vi ass/hello.s
    ```

3.  **Build and Run:**

    Navigate to the project directory and run the setup script. This
    script handles the `aclocal`, `autoreconf`, `configure`, and
    `make` pipeline automatically. 
    
    *(Note: You must be on an ARM64 system or emulator to run the compiled assembly binary).*
    
    ```sh
    cd ass
    chmod +x setup.sh
    ./setup.sh
    ```

## License

*Feel free to use snippets from this repository for your own practice.*