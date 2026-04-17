import time
import tracemalloc

# --- GREEN AI EFFICIENCY TRACKER ---
# This function measures time and memory, showing the "environmental cost"
def measure_efficiency(func, data, target):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = func(data, target)
    
    end_time = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"\n>>> Results for: {func.name}")
    print(f"Execution Time: {end_time - start_time:.8f} seconds")
    print(f"Peak Memory: {peak_memory / 10**6:.6f} MB")
    return result

# --- APPROACH 1: LINEAR SEARCH (High Carbon Footprint) ---
# It checks every single item. If the data is at the end, it wastes a lot of energy.
def linear_search(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

# --- APPROACH 2: BINARY SEARCH (Green/Efficient Approach) ---
# It divides the data in half repeatedly. Much faster and eco-friendly!
def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == target:
            return mid
        elif data_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- PERFORMANCE TEST ---
print("Generating 10 million data points...")
large_dataset = list(range(10000000))
search_target = 9999999 

print("\nStarting Environmental Impact Tests...")
# Testing the slow way
measure_efficiency(linear_search, large_dataset, search_target)
# Testing the green way
measure_efficiency(binary_search, large_dataset, search_target)
