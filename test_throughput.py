import time

# Define a function that performs an operation (e.g., processing a request)


def perform_operation(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


# Measure throughput by counting the number of operations per second
num_operations = 100_000
start_time = time.time()
perform_operation(num_operations)
end_time = time.time()
try:
    elapsed_time = end_time - start_time
    throughput = num_operations / elapsed_time
except ZeroDivisionError:
    print("Elapsed time is near zero.Try increasinf num_operations by tenth!")
else:
    print(f"Throughput: {throughput:.2f} operations per second")
