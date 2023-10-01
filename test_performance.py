""" 
    Test performance for CPU intensive task
"""
import time

def perform_calculation(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def test_processor(itter:int, work_load:int)-> list[float]:
    execution_result = []
    for i in range(itter):
        start_time = time.time()
        result = perform_calculation(work_load)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_result.append(execution_time)
    return list(map(lambda x: round(x, 6), execution_result))

if __name__ == "__main__":
    res = test_processor(10, 1000000)
    print(f"Results in secs:\n {res}")
