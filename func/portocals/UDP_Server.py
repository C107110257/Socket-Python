import socket
import threading

from func.config import *
from func.ths.sk_thread_udp import create_udp_recv_thread, udp_peer
from func.send_recv.sk_send import send_msg


def run_udp_server(host="::", port=DEFAULT_PORT, verbose=False):

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6,socket.IPV6_V6ONLY,0)
    
    sock.bind((host, port))

    print(f"UDP Listen on {host}:{port}")

    stop_event = threading.Event()

    create_udp_recv_thread(sock, "Client", PROMPT["UDP_SERVER"], stop_event)

    while not stop_event.is_set():

        msg = input(PROMPT["UDP_SERVER"])

        if msg.lower() == "exit":
            break

        if udp_peer["addr"]:
            # print(f"Send To => {udp_peer['addr']}")
            send_msg(sock, msg, protocol="udp", addr=udp_peer["addr"])
            # print("send ok")

    sock.close()
