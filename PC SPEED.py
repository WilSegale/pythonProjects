import timeit
import psutil
import platform

# Define a simple function to measure
def test_function():
    total = 0
    for i in range(10000):
        total += i
    return total

# Measure the execution time
execution_time = timeit.timeit(test_function, number=1000)
print(f"Execution time: {execution_time:.6f} seconds")

# Get CPU frequency
cpu_freq = psutil.cpu_freq()
print(f"Current CPU frequency: {cpu_freq.current:.2f} MHz")
print(f"Max CPU frequency: {cpu_freq.max:.2f} MHz")
print(f"Min CPU frequency: {cpu_freq.min:.2f} MHz")

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU usage: {cpu_usage}%")

# Get processor information
processor = platform.processor()
print(f"Processor: {processor}")
