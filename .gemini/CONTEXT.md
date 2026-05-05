# Eternal Torment Repository Summary

## Overview
**Repository:** `pale-shadow/eternal-torment`
**Purpose:** A high-entropy sandbox dedicated to low-level coding practice, build-system experimentation, and continuous technical refinement.
**Context:** As a core component of the `pale-shadow` GitHub organization, this repository acts as the proving ground for tools that eventually migrate into more structured projects like the "Hacker Cookbook" or "Stash House." It bridges the gap between CTF tool development and functional system administration.

---

## Recent Updates and Experiments
Recent activity by **devsecfranklin** reflects a pivot toward hardware-accelerated computing and bare-metal interaction:

* **AArch64 Assembly (`ass/`):** Implementation of AArch64 `write(2)` system calls within `hello.s`. This serves as a baseline for understanding ARM64 performance on edge hardware.
* **HPC & Clustering (`lab.bitsmasher.net`):** Active development of "Ignite" scripts to refresh a **4-node NVIDIA Jetson cluster**. This includes shimming the NVIDIA Container Runtime into **K3s** to facilitate GPU-accelerated numerical processing.
* **Numerical Computation:** Experimenting with distributed math engines. The current performance metric for cluster throughput is modeled as:
    $$P_{total} = \sum_{i=1}^{n} (N_{cores, i} \times f_{i} \times \text{FLOPS}_{cycle})$$
* **GNU Autotools:** Refining dynamic build environments using `configure.ac` and `Makefile.am`. This pipeline is being standardized to ensure portability across Debian and OpenBSD environments.

---

## Repository Structure
The repository structure is designed for rapid prototyping and environment consistency:

* **Environment & Runtime:** `.gemini`, `.github`, `.vscode`, and `.devcontainer` for seamless transitions between local `vi` sessions and remote GKE/Jetson environments.
* **Source & Binaries:** `bin`, `src`, and `include` directories for C and Assembly source management.
* **Documentation & Templates:** `docs/`, `static/`, and `drawio-nn-templates` for mapping out cluster architecture diagrams.
* **Experimental Vault:** `HAHAFUN` and `palm-api` for one-off API tests and chaotic script storage.

---

## Technical Stack & Languages
The stack remains heavily weighted toward systems-level programming, emphasizing control and efficiency:

| Language | Percentage | Focus Area |
| :--- | :--- | :--- |
| **Assembly** | 24.1% | AArch64 system calls, ARM64 optimization |
| **C** | 22.8% | Systems tools and core utilities |
| **Python** | 21.5% | Automation, API interaction, and rapid testing |
| **Shell** | 7.6% | `bash` and `ksh` deployment scripts |
| **Makefile** | 3.9% | Autotools and build orchestration |
| **Other** | 20.1% | Roff, YAML, and LaTeX documentation |

---

## License and Maintainers
* **Maintainer:** devsecfranklin (Franklin D.)
* **Organization:** Pale Shadow
* **License:** Apache-2.0 License

---

## Getting Started
To initialize the current testing environment:

1.  **Clone the Repo:** `git clone https://github.com/pale-shadow/eternal-torment.git`
2.  **Configure:** Navigate to the `ass/` or `src/` directory. Use `vi` to inspect the source.
3.  **Ignite:** Run the `setup.sh` script. This triggers the `autoreconf -i` and `configure` pipeline, preparing the environment for the local architecture.
4.  **Execute:** Ensure you are running on an **ARM64** target (like the Jetson cluster) if testing AArch64 assembly binaries.

> **Note:** For cluster-wide deployments, ensure the `KUBECONFIG` is pointed to the master node of the `bitsmasher.net` lab.