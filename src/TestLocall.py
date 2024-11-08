# Test.py
from annotation import locall_function
from connexus import start_server
import threading

@locall_function
def add(a, b):
    return a + b

@locall_function
def subtract(a, b):
    return a - b

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()