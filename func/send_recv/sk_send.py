import json


def send_msg(
        sock,
        msg,
        protocol="tcp",
        addr=None):

    if isinstance(msg, dict):

        msg = json.dumps(msg)

    if isinstance(msg, str):

        msg = msg.encode()

    if protocol == "tcp":

        sock.send(msg)

    elif protocol == "udp":

        sock.sendto(msg, addr)