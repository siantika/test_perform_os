import time
import statistics


def perform_operation(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


def measure_throughput(operation_function, work_load, num_repeats):
    throughputs = []  # Store individual throughput values for calculating standard deviation
    for _ in range(num_repeats):
        start_time = time.time()
        operation_function(work_load)
        end_time = time.time()
        elapsed_time = end_time - start_time
        try:
            throughput = work_load / elapsed_time
        except ZeroDivisionError:
            print(
                "Elapsed time is near zero. Try increasing num_operations or reducing num_repeats.")
            return None
        throughputs.append(throughput)

    average_throughput = sum(throughputs) / num_repeats
    std_deviation = statistics.stdev(throughputs) if num_repeats > 1 else 0

    return average_throughput, std_deviation


if __name__ == "__main__":
    work_load_1 = 10_000
    work_load_2 = 100_000
    work_load_3 = 1_000_000
    num_repeats = 10

    result_1 = measure_throughput(perform_operation, work_load_1, num_repeats)
    result_2 = measure_throughput(perform_operation, work_load_2, num_repeats)
    result_3 = measure_throughput(perform_operation, work_load_3, num_repeats)

    if (result_1 and result_2 and result_3) is not None:
        average_throughput_1, std_deviation_1 = result_1
        average_throughput_2, std_deviation_2 = result_2
        average_throughput_3, std_deviation_3 = result_3
        print("Workload: 10.000")
        print(
            f"Average Throughput: {average_throughput_1:.2f} operations per second")
        print(
            f"Standard Deviation: {std_deviation_1:.2f} operations per second (across {num_repeats} runs)")
        print("\n")
        print("Workload: 100.000")
        print(
            f"Average Throughput: {average_throughput_2:.2f} operations per second")
        print(
            f"Standard Deviation: {std_deviation_2:.2f} operations per second (across {num_repeats} runs)")
        print("\n")
        print("Workload: 1.000.000")
        print(
            f"Average Throughput: {average_throughput_3:.2f} operations per second")
        print(
            f"Standard Deviation: {std_deviation_3:.2f} operations per second (across {num_repeats} runs)")
        print("\n")
