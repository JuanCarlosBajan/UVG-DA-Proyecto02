import time

def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize the maximum sum to negative infinity
    s = 0  # Initialize the current sum to 0
    start_index = 0  # Initialize the start index of the maximum subarray
    end_index = 0  # Initialize the end index of the maximum subarray
    temp_start_index = 0  # Temporary start index for updating the maximum subarray

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

        if current_sum < 0:
            current_sum = 0
            temp_start_index = i + 1

    max_subarray = arr[start_index:end_index+1]
    return max_sum, max_subarray


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

start_time = time.time()
for x in range(0,1000):
    max_sum, subarray = max_subarray_sum(arr)
end_time = time.time()
execution_time = end_time - start_time

print("Suma máxima:", max_sum)
print("Subarreglo:", subarray)
print("Tiempo de ejecución:", execution_time, "segundos")