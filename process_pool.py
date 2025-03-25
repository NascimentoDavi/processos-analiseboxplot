# Pool serve para criar processos que podem ser reutilizados, evitando o custo de tempo e recurso de recria-los.

from multiprocessing import Pool
import os

def square(n):
    return (os.getpid(), n, n * n)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    with Pool(2) as pool:
        results = pool.map(square, numbers)
    for pid, n, sq in results:
        print("Processo", pid, "calculou o quadrado de", n, "=", sq)

        