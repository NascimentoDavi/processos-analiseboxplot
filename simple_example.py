from multiprocessing import Process
import time

def long_running_task():
    print("Starting task...")
    time.sleep(1)
    print("Finishing task...")

if __name__ == "__main__":
    process_1 = Process(target=long_running_task)
    process_2 = Process(target=long_running_task)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    # metodo join garante que o processo principal aguarde a conclusao dos processos filhos antes de prosseguir.

    print("All the processes are done")