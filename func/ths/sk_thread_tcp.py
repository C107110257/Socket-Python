import threading


def recv_worker(sock, peer_name, prompt, stop_event):

    while not stop_event.is_set():

        try:

            data = sock.recv(1024)

            if not data:
                print(f"\n[INFO] From {peer_name} disconnected")
                stop_event.set()
                break

            print(f"\n From {peer_name}: {data.decode()}")
            print(prompt, end="", flush=True)

        except Exception as e:

            print(f"\n[ERROR] {e}")
            stop_event.set()
            break


def create_recv_thread(sock, peer_name, prompt, stop_event):

    rx = threading.Thread(
        target=recv_worker, args=(sock, peer_name, prompt, stop_event), daemon=True
    )

    rx.start()

    return rx
