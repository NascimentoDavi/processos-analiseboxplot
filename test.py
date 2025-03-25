from multiprocessing import Process
import time

def greeting(message):
    time.sleep(5)
    print(message)

process_with_args = Process(target=greeting, args=("Hello, World!",))

process_with_args.start()
print("Process running: ", process_with_args.is_alive())

process_with_args.join() # Waits for the process conclusion
print("Process ended: ", not process_with_args.is_alive())
