#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFF_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, sockettype, proto, canonname, sockaddr) = addr_info[0]



def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((HOST, PORT))
        sock.listen(1)
        while True:
            conn, addr = sock.accept()
            with conn:
                with socket.socket(family, sockettype) as proxy_end:
                    proxy_end.connect(sockaddr)

                    data = b""
                    while True:
                        tmp_data = conn.recv(BUFF_SIZE)
                        if not tmp_data:
                            break
                        data += tmp_data

                    proxy_end.sendall(data)

                    google_data = b""
                    while True:
                        tmp_data = proxy_end.recv(BUFF_SIZE)
                        if not tmp_data:
                            break
                        google_data += tmp_data
                    conn.sendall(google_data)

if __name__ == "__main__":
    main()
