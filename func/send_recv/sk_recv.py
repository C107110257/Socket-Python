import json


def recv_msg(
        sock,
        protocol="tcp",
        bufsize=1024):

    if protocol == "tcp":

        data = sock.recv(bufsize)

        return data.decode()

    elif protocol == "udp":

        data, addr = sock.recvfrom(bufsize)

        return data.decode(), addr