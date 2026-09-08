import socket


def get_ip_family(ip):

    try:
        socket.inet_pton(
            socket.AF_INET,
            ip
        )

        return socket.AF_INET

    except OSError:
        pass

    try:
        socket.inet_pton(
            socket.AF_INET6,
            ip
        )

        return socket.AF_INET6

    except OSError:
        pass

    raise ValueError(
        f"Invalid IP address: {ip}"
    )