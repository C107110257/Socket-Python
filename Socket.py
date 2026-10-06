from func.args_parse import get_args
from func.protocols.TCP_Client import run_client
from func.protocols.TCP_Server import run_server
from func.protocols.UDP_Client import run_udp_client
from func.protocols.UDP_Server import run_udp_server


def main():

    args = get_args()
    print(args)
    if args.type == "tcp":

        if args.server:
            run_server(
                port=args.port,
                verbose=args.verbose
            )

        elif args.client:
            run_client(
                args.client,
                args.port,
                args.verbose
            )

    elif args.type == "udp":

        if args.server:
            run_udp_server(
                port=args.port,
                verbose=args.verbose
            )

        elif args.client:
            run_udp_client(
                args.client,
                args.port,
                args.verbose
            )


if __name__ == "__main__":
    main()
