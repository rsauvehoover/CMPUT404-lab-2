#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFF_SIZE = 1024

def handle_echo(conn,addr):
    with conn:
       print(conn)
       full_data = b""
       while True:
           data = conn.recv(BUFFER_SIZE)
           if not data:
               break
           full_data += data
       time.sleep(0.5)
       conn.sendall(full_data)
       conn.shutdown(socket.SHUT_RDWR)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      

        s.bind((HOST, PORT))
        s.listen(1) 
       
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(conn, addr))
            p.daemon = True
            p.start()

if __name__ == "__main__":
    main()
