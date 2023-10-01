import subprocess
import time

def get_gpu_metrics():
    try:
        # Run the "nvidia-smi" command and capture its output
        result = subprocess.run(["nvidia-smi", "--query-gpu=memory.used,memory.total,utilization.gpu", "--format=csv,noheader,nounits"], stdout=subprocess.PIPE, text=True)

        # Split the output into individual values
        metrics = result.stdout.strip().split(', ')

        # Extract Memory-Usage and GPU-Util values
        memory_usage = int(metrics[0])
        gpu_utilization = int(metrics[2])

        return memory_usage, gpu_utilization

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        return None, None

def main(interval_seconds=2):
    while True:
        memory_usage, gpu_utilization = get_gpu_metrics()

        if memory_usage is not None and gpu_utilization is not None:
            # Print Memory-Usage and GPU-Util on the same line
            print(f"Memory-Usage: {memory_usage} MiB, GPU-Util: {gpu_utilization}%", end='\r')

        # Wait for the specified interval before the next update
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()