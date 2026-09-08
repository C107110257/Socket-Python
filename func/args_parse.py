import argparse
from func.config import *


def get_args():

    parser = argparse.ArgumentParser(
        prog="Socket.py",
        description="TCP/UDP Socket Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument(
        "-s",
        "--server",
        action="store_true",
        help="Run as server"
    )

    mode.add_argument(
        "-c",
        "--client",
        metavar="SERVER_IP",
        help="Run as client"
    )

    parser.add_argument(
        "-t",
        "--type",
        default="tcp",
        choices=["tcp", "udp"],
        help="Protocol type"
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help="Port number"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose mode"
    )

    return parser.parse_args()