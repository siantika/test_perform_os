import statistics
import psutil
import time

# Function to get disk I/O throughput in MB/s


def get_disk_io_throughput():
    initial_io_counters = psutil.disk_io_counters()
    time.sleep(1)  # Sleep for 1 second
    final_io_counters = psutil.disk_io_counters()

    # Calculate the change in bytes read and written over the 1-second interval
    bytes_read = final_io_counters.read_bytes - initial_io_counters.read_bytes
    bytes_written = final_io_counters.write_bytes - initial_io_counters.write_bytes

    throughput_b_per_s = (bytes_read + bytes_written)

    return throughput_b_per_s


def test_processor(itter: int):
    # Using buffer to minimize impact of writing to disk
    disk_io_throughputs = []
    for _ in range(itter):
        disk_io_throughput = get_disk_io_throughput()
        disk_io_throughputs.append(disk_io_throughput)
    return disk_io_throughputs


def result_statistic(data: list):
    avg_data = statistics.mean(data)
    min_data = min(data)
    max_data = max(data)
    std_deviation = statistics.stdev(data)

    return {
        "Average throughput (bytes/s)": round(avg_data, 2),
        "Minimum throughput (bytes/s)": round(min_data, 2),
        "Maximum throughput (bytes/s)": round(max_data, 2),
        "Standard Deviation (bytes/s)": round(std_deviation, 2)
    }


if __name__ == '__main__':
    data_test = test_processor(10)
    result = result_statistic(data_test)
    print("Disk I/O Throughput:")
    for key, value in result.items():
        print(f"{key}: {value}")
