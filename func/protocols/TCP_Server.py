import socket
import threading
from func.config import *
from func.ths.sk_thread_tcp import create_recv_thread
from func.send_recv.sk_send import send_msg


def run_server(host="::", port=DEFAULT_PORT, verbose=False):

    print("run_server()")

    server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setsockopt(socket.IPPROTO_IPV6,socket.IPV6_V6ONLY,0)


    print("socket created")

    server.bind((host, port))

    print("bind ok")

    server.listen()

    print(f"Listen on {host}:{port}")

    conn, addr = server.accept()
    print(f"Connected from {addr}")

    stop_event = threading.Event()

    create_recv_thread(conn, "Client", PROMPT["TCP_SERVER"], stop_event)
    try:

        while not stop_event.is_set():

            msg = input(PROMPT["TCP_SERVER"])

            if stop_event.is_set():
                break

            if msg.lower() == "exit":
                break

            try:
                send_msg(conn, msg, protocol="tcp")

            except Exception as e:
                print(f"\n[ERROR] {e}")
                break

    finally:

        conn.close()
        server.close()

        print("Server closed")
