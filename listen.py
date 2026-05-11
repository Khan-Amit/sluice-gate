# listen.py - send/receive through any channel

import socket
import requests

class Channel:
    @staticmethod
    def send(data: bytes, target: str, protocol: str = "tcp"):
        if protocol == "tcp":
            host, port = target.split(":")
            sock = socket.socket()
            sock.connect((host, int(port)))
            sock.send(data)
            sock.close()
        elif protocol == "https":
            requests.post(target, data=data, verify=False)

    @staticmethod
    def receive(port: int) -> bytes:
        server = socket.socket()
        server.bind(("127.0.0.1", port))
        server.listen(1)
        conn, _ = server.accept()
        data = conn.recv(4096)
        conn.close()
        return data
