import multiprocessing

work_load = 10000000
# Define a CPU-intensive function


def cpu_intensive_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()  # Get the number of CPU cores

    # Start multiple processes to simulate CPU load
    processes = [multiprocessing.Process(
        target=cpu_intensive_task, args=(work_load,)) for _ in range(num_processes)]

    # Start the processes
    for process in processes:
        process.start()

    # Monitor CPU usage while the processes are running
    try:
        # You can use external tools like 'top', 'htop', or system-specific utilities
        # to monitor CPU usage, or use Python libraries like psutil to monitor it programmatically.
        # Here's a basic example using psutil:
        import psutil
        # Check CPU usage every 1 second
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_percent}%")
    except KeyboardInterrupt:
        # Stop the processes if the user interrupts the script (e.g., by pressing Ctrl+C)
        for process in processes:
            process.terminate()
            process.join()

    # Wait for all processes to finish
    for process in processes:
        process.join()
