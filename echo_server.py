#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFF_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((HOST, PORT))
        sock.listen(1)
        while True:
            conn, addr = sock.accept()
            data = b""
            while True:
                tmp_data = conn.recv(BUFF_SIZE)
                if not tmp_data:
                    break
                data += tmp_data
            conn.sendall(data)

if __name__ == "__main__":
    main()
