import time
import statistics

def perform_calculation(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def test_processor(iterations: int, work_load: int) -> dict:
    execution_times = []
    for i in range(iterations):
        start_time = time.time()
        result = perform_calculation(work_load)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    
    avg_execution_time = statistics.mean(execution_times)
    min_execution_time = min(execution_times)
    max_execution_time = max(execution_times)
    std_deviation = statistics.stdev(execution_times)
    
    return {
        "Average Execution Time (secs)": round(avg_execution_time, 6),
        "Minimum Execution Time (secs)": round(min_execution_time, 6),
        "Maximum Execution Time (secs)": round(max_execution_time, 6),
        "Standard Deviation (secs)": round(std_deviation, 6)
    }

if __name__ == "__main__":
    iterations = 20
    work_load_1 = 10_000
    work_load_2 = 100_000
    work_load_3 = 1_000_000
    
    results_1 = test_processor(iterations, work_load_1)
    print("Pengujian dengan workload 10.000")
    print(40*"-")
    for key, value in results_1.items():
        print(f"{key}: {value}")
    print("\n")

    time.sleep(1)
    results_2 = test_processor(iterations, work_load_2)
    print("Pengujian dengan workload 100.000")
    print(40*"-")
    for key, value in results_2.items():
        print(f"{key}: {value}")
    print("\n")

    time.sleep(1)
    results_3 = test_processor(iterations, work_load_3)
    print("Pengujian dengan workload 1.000.000")
    print(40*"-")
    for key, value in results_3.items():
        print(f"{key}: {value}")
    print("\n")

