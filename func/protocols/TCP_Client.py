import socket
import threading
from func.config import *
from func.ths.sk_thread_tcp import create_recv_thread
from func.send_recv.sk_send import send_msg
from func.ip_handler.sk_ip import get_ip_family

def run_client(server_ip, port=DEFAULT_PORT, verbose=False):

    print("run_client()")

    family = get_ip_family(server_ip)
    
    sock = socket.socket(family, socket.SOCK_STREAM)

    print("socket created")

    sock.connect((server_ip, port))

    print(f"Connected to {server_ip}:{port}")

    stop_event = threading.Event()

    create_recv_thread(sock, "Server", PROMPT["TCP_CLIENT"], stop_event)
    try:
        while not stop_event.is_set():

            msg = input(PROMPT["TCP_CLIENT"])

            if stop_event.is_set():
                break

            if msg.lower() == "exit":
                break

            try:
                send_msg(sock, msg, protocol="tcp")

            except Exception as e:
                print(f"\n[ERROR] {e}")
                break

    finally:
        sock.close()

        print("Client closed")
