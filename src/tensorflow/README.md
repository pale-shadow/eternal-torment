# TensorFlow Experiments

This directory serves as a sandbox for machine learning experimentation on edge hardware, specifically targeting the NVIDIA Jetson Nano 2GB Developer Kit. The goal is to optimize model training and inference within a resource-constrained environment while leveraging GPU acceleration.

## Environment Architecture

Experiments are designed to run within an orchestrated Kubernetes environment (K3s/GKE) using the NVIDIA Container Runtime.

* **Base Image:** `nvcr.io/nvidia/l4t-tensorflow:r32.6.1-tf2.5-py3`
* **Hardware Target:** NVIDIA Jetson Nano 2GB (Maxwell GPU / AArch64)
* **Orchestration:** Kubernetes Pods with Node Affinity for hardware-specific scheduling.

## Key Components

* `tf.py`: A verification script to ensure the TensorFlow build correctly recognizes the Maxwell GPU and to manage memory growth.
* `tf-pod.yaml`: Kubernetes manifest defining pod specifications, including node affinity and resource constraints.
* `requirements.txt`: Python dependencies optimized for the Linux for Tegra (L4T) environment.
* `tensorflow.md`: Historical logs and troubleshooting notes regarding dependency resolution and JetPack versioning.

## Setup and Configuration

### 1. Build the Optimized Container
Utilize the modernized Dockerfile in the repository root to build the image. Ensure BuildKit is enabled to take advantage of layer caching for APT and PIP.

```bash
# From the repository root
docker build -t <your-registry>/tf-jetson:latest .