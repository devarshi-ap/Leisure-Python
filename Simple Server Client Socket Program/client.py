import socket

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.connect((socket.gethostname(), 5050))
header_size = 10

while True:
    full_msg = ''

    new_msg = True
    while True:
        msg = SERVER.recv(10)
        if new_msg:
            print(f"new message length: {msg[:header_size]}")
            msg_length = int(msg[:header_size])
            new_msg = False

        full_msg += msg.decode('utf-8')

        if len(full_msg) - header_size == msg_length:
            print("entire message received")
            print(full_msg[header_size:])
            new_msg = True
            full_msg = ''

    print(full_msg)

