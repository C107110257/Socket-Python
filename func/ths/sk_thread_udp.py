import threading

udp_peer = {"addr": None}


def udp_recv_worker(sock, peer_name, prompt, stop_event):

    print("UDP recv thread start")

    while not stop_event.is_set():

        try:

            # print("waiting udp packet...")

            data, addr = sock.recvfrom(1024)

            # print("udp packet arrived")
            if not data:
                print(f"\n[INFO] From {peer_name} disconnected")
                stop_event.set()
                break

            if udp_peer["addr"] != addr:
                
                udp_peer["addr"] = addr

                # print("\n========== UDP Peer Updated ==========")
                # print(f"IP : {addr[0]}")
                # print(f"PORT : {addr[1]}")
                # print(f"ADDR : {addr}")
                # print("======================================")

            print(f"\n From {peer_name} {addr}: " f"{data.decode()}")

            print(prompt, end="", flush=True)

        except Exception as e:

            print(f"\n[ERROR] {e}")

            stop_event.set()

            break


def create_udp_recv_thread(sock, peer_name, prompt, stop_event):

    rx = threading.Thread(
        target=udp_recv_worker, args=(sock, peer_name, prompt, stop_event), daemon=True
    )

    rx.start()

    return rx
