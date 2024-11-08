# connexus.py

import socket
import json
from locall_context import LocallContext

def start_server(host='127.0.0.1', port=8082):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                try:
                    message = json.loads(data.decode())
                    func_name = message["function"]
                    args = message["args"]

                    # 使用LocallContext进行方法调用
                    result = LocallContext.call_function(func_name, args)
                    if result is None:
                        result = "Error: Unknown function"
                except (json.JSONDecodeError, KeyError):
                    result = "Error: Invalid JSON format"

                client_socket.sendall((result + "\n").encode())