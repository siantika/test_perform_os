import psutil
import statistics


def cpu_intensive_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


def test_processor(workload: int, num_samples: int, interval: float):
    cpu_usages = []
    for _ in range(num_samples):
        cpu_usage_start = psutil.cpu_percent(interval=interval)
        cpu_intensive_task(workload)
        cpu_usage_end = psutil.cpu_percent(interval=interval)
        cpu_usage_diff = cpu_usage_end - cpu_usage_start
        cpu_usages.append(cpu_usage_diff)

    # Calculate statistics
    avg_cpu_usage = sum(cpu_usages) / num_samples
    min_cpu_usage = min(cpu_usages)
    max_cpu_usage = max(cpu_usages)
    std_deviation = statistics.stdev(cpu_usages)

    print(
        f"Average CPU Usage over {interval * num_samples} seconds: {avg_cpu_usage:.2f}%")
    print(f"Minimum CPU Usage: {min_cpu_usage:.2f}%")
    print(f"Maximum CPU Usage: {max_cpu_usage:.2f}%")
    print(f"Standard Deviation of CPU Usage: {std_deviation:.2f}")


if __name__ == '__main__':
    workload_1 = 10_000
    workload_2 = 100_000
    workload_3 = 1_000_000
    num_samples = 10
    interval = 1.0

    print("Workload 10.000")
    test_processor(workload_1, num_samples, interval)
    print()
    print("Workload 100.000")
    test_processor(workload_2, num_samples, interval)
    print()
    print("Workload 1.000.000")
    test_processor(workload_3, num_samples, interval)
