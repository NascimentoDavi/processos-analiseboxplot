from multiprocessing import Process
import os
import time

# Each process has its memory space and identifier

# This technique is used to monitore and depure paralel processes execution

def show_ids():
    print("Child: PID = ", os.getpid(), "PPID = ", os.getppid())
    time.sleep(1)
    print("Child ending: PID = ", os.getpid())

if __name__ == "__main__":
    print("Parent: PID = ", os.getpid())
    p1 = Process(target=show_ids)
    p2 = Process(target=show_ids)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Parent process ended")