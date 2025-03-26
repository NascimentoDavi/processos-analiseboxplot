import time
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np


# VERSÃO SEQUENCIAL
# Recursive calls to sort both halves
# Single threaded execution - only one process is working on sorting
# Time complexity O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)  # Ensure the sorted half is returned
        right_half = merge_sort(right_half)  # Ensure the sorted half is returned

        return merge(left_half, right_half)  # Merge and return the result
    return arr  # Return the array if its length is 1 or less


# VERSÃO PARALELA
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # merge_sort(left_half) is running in one process
    # merge_sort(right_half)is running in another process
    with multiprocessing.Pool(processes=2) as pool:
        left_sorted, right_sorted = pool.map(merge_sort, [left_half, right_half])
    
    # After both sides are sorted in parallel, they are merged into a single sorted list
    return merge(left_sorted, right_sorted)


# Takes two sorted lists and merges them into a single sorted list
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ACESS AND MODIFY FILES TO GET THE NUMBERS
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]


# WRITE THE NUMBERS INTO THE FILE
def write_numbers_to_file(file_path, numbers):
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")


# Measures the execution time of a given sorting function over multiple iterations
# It records the time taken for each execution and returns a list of execution times.
def benchmark_sorting(sorting_function, numbers, iterations=10):
    times = []
    for _ in range(iterations):
        numbers_copy = numbers[:]
        start_time = time.perf_counter()

        sorting_function(numbers_copy)

        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

def plot_results(seq_times, par_times):
    plt.figure(figsize=(12, 6))
    plt.boxplot([seq_times, par_times], labels=["Sequencial", "Paralelo"])
    plt.ylabel("Tempo (s)")
    plt.title("Comparação de Tempo - Merge Sort Sequencial vs Paralelo")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_file = "../Listas/listas/listas_pequenas/100.txt"
    numbers = read_numbers_from_file(input_file)

    # Medindo tempos de execução
    seq_times = benchmark_sorting(merge_sort, numbers)
    par_times = benchmark_sorting(parallel_merge_sort, numbers)

    # Salvando os números ordenados após a versão sequencial
    sorted_numbers = numbers[:]
    merge_sort(sorted_numbers)
    write_numbers_to_file("numeros_ordenados.txt", sorted_numbers)

    print("Ordenação concluída! Comparando tempos...")
    
    # Gerando box plots
    plot_results(seq_times, par_times)
