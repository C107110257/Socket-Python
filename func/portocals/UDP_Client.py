import socket
import threading

from func.config import *
from func.ths.sk_thread_udp import create_udp_recv_thread
from func.send_recv.sk_send import send_msg
from func.ip_handler.sk_ip import get_ip_family

def run_udp_client(server_ip, port=DEFAULT_PORT, verbose=False):

    family = get_ip_family(server_ip)

    sock = socket.socket(family, socket.SOCK_DGRAM)

    print(f"UDP connected to " f"{server_ip}:{port}")

    stop_event = threading.Event()

    create_udp_recv_thread(sock, "Server", PROMPT["UDP_CLIENT"], stop_event)

    while not stop_event.is_set():

        msg = input(PROMPT["UDP_CLIENT"])

        if msg.lower() == "exit":
            break

        send_msg(sock, msg, protocol="udp", addr=(server_ip, port))

    sock.close()
