from multiprocessing import Process
import time
import math

# EXECUÇÃO SEQUENCIAL X EXECUÇÃO PARALELA

# ESPERA-SE QUE A ABORDAGEM PARALELA SEJA MAIS RÁPIDA, POIS DIVIDE A CARGA DE TRABALHO ENTRE MÚLTIPLOS NÚCLEOS.l

    def calcular_operacao_intensiva(n):
    for _ in range(100):
        result = math.factorial(30000)
    print(f"Processo {n} completou operações intensivas")

if __name__ == "__main__":
    inicio_paralelo = time.perf_counter()

    p1 = Process(target=calcular_operacao_intensiva, args=(1,))
    p2 = Process(target=calcular_operacao_intensiva, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    fim_paralelo = time.perf_counter()

    # Versão Sequencial
    inicio_sequencial = time.perf_counter()

    calcular_operacao_intensiva(3)

    time.sleep(2)

    calcular_operacao_intensiva(4)

    fim_sequencial = time.perf_counter()

    # Resultados
    print(f"Tempo paralelo: {fim_paralelo - inicio_paralelo:.2f} segundos")
    print(f"Tempo sequencial: {fim_sequencial - inicio_sequencial:.2f} segundos")

    diferenca = (fim_sequencial - inicio_sequencial) - (fim_paralelo - inicio_paralelo)
    print(f"Diferença: {diferenca:.2f} segundos a favor do paralelismo")

# Abordagem paralela é mais rápida, pois divide a carga de trabalho entre multiplos nucleos
