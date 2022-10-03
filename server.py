from audioop import reverse
from concurrent.futures import thread
import socket
import threading

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 100
FORMAT = 'utf_8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    connected = True
    conn.send("Thank for connecting".encode(FORMAT))
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            break

    conn.send('Generate random set of numbers 25 values between 1 and 100?'.encode(FORMAT))

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            numbers = eval(msg)
            numbers.sort()
            conn.send(str(numbers).encode(FORMAT))
            break

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            newList= msg.split(" ")
            conn.send(f'hello {newList[3]},Glad to meet you?'.encode(FORMAT))


    conn.close()



def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[Active connections] {threading.active_count() - 1}')

print("[STARTING] server is starting....")
start()

