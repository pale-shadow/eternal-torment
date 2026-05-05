import tensorflow as tf

def check_gpu():
    # List physical devices recognized by the CUDA-linked TF
    gpus = tf.config.list_physical_devices('GPU')
    
    if gpus:
        try:
            # Recommended for Jetson: Prevent TF from hogging all 2GB VRAM immediately
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            print(f"Found {len(gpus)} GPU(s): {gpus}")
        except RuntimeError as e:
            print(e)
    else:
        print("No GPU detected. Check NVIDIA Container Runtime / K8s Node Affinity.")

if __name__ == "__main__":
    check_gpu()
    # Print the specific device name (e.g., /device:GPU:0)
    print("Available devices:", [d.name for d in tf.config.list_logical_devices()])