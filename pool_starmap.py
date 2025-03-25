#  Utilizamos starmap quando a função precisa de mais de um argumento

from multiprocessing import Pool
import time

def calcular_potencia(base, expoente):
    return base ** expoente;

if __name__ == "__main__":
    # Lista de Tuplas onde cada tupla contem (base, expoente)
    argumentos = [(2,5), (3,4), (5,3), (7,2), (10,6), (8,3)]

    with Pool(processes=3) as pool:
        inicio = time.perf_counter()
        results = pool.starmap(calcular_potencia, argumentos)
        fim = time.perf_counter()

    print("Resultados:", results)
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")

