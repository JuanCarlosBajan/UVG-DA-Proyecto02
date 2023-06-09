import time
import ast

def max_subarray_sum(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]  # La suma máxima de un subarreglo de un solo elemento es ese elemento en sí
    max_sum = dp[0]  # Inicializamos el máximo con el primer elemento
    start_index = 0
    end_index = 0

    for i in range(1, n):
        if arr[i] > dp[i-1] + arr[i]:
            dp[i] = arr[i]
            start_index = i  # Actualizamos el inicio del nuevo subarreglo
        else:
            dp[i] = dp[i-1] + arr[i]

        if dp[i] > max_sum:
            max_sum = dp[i]
            end_index = i  # Actualizamos el final del subarreglo con la nueva suma máxima

    max_subarray = arr[start_index:end_index+1]
    return max_sum, max_subarray

with open('entrada.txt', 'r') as input_file, open('tiempos2.txt', 'w') as output_file:
    for line in input_file:
        try:
            arr = ast.literal_eval(line.strip())
            arr = list(map(int, arr))

            start_time = time.time()
            for x in range(0, 1000):
                max_sum, subarray = max_subarray_sum(arr)
            end_time = time.time()
            execution_time = end_time - start_time

            output_file.write(str(execution_time) + '\n')

            print("Arreglo de entrada:", arr)
            print("Suma máxima:", max_sum)
            print("Subarreglo:", subarray)
            print("Tiempo de ejecución:", execution_time, "segundos")
            print()
        except Exception as e:
            print("Error en la línea:", line)
            print("Error:", e)
            print()