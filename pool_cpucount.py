from multiprocessing import Pool, cpu_count
import time
import math

def calcular_fatorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [50000, 40000, 30000, 20000, 10000, 5000]

    # Obtém o número de núcleos disponíveis na CPU
    num_processos = cpu_count()
    print(f"Usando {num_processos} processos")

    with Pool(processes=num_processos) as pool:
        inicio = time.perf_counter()

        results = pool.map(calcular_fatorial, numbers)

        fim = time.perf_counter()

    print("Resultados calculados")
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")