#!/usr/bin/env python3
import socket

HOST = "www.google.com"
PORT = 80
BUFF_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {host}

""".format(host=HOST)

def connect_sock(addr):
    (family, socktype, proto, cannoname, sockaddr) = addr
    try:
        sock = socket.socket(family, socktype, proto)
        sock.connect(sockaddr)
        sock.sendall(payload.encode())

        data = b""
        while True:
            tmp_data = sock.recv(BUFF_SIZE)
            if not tmp_data:
                break
            data += tmp_data
        print(data)
    except:
        print("Failed to connect to {host}".format(host=HOST))
    finally:
        sock.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_sock(addr)

if __name__ == "__main__":
    main()
