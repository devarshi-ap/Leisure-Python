import socket
import time


HOST = socket.gethostname()
PORT = 5050
header_size = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5) # queue of 5

    while True:
        conn, address = s.accept()
        print(f"[CONNECTED] Connected to client from ipv4: {address}")

        msg = "Welcome to the server broski!"
        msg = f"{len(msg):<{header_size}}" + msg

        conn.send(bytes(msg, "utf-8"))

        while True:
            time.sleep(3)
            msg = f"Broski do u know what time it is? Yeah Fam its: {time.time()}"
            msg = f"{len(msg):<{header_size}}" + msg
            conn.send(msg.encode(encoding='UTF-8'))
