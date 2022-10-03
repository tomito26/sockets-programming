import random
import socket

HEADER = 100
FORMAT = 'utf_8'
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) 

print(client.recv(2048).decode(FORMAT))




def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

random_numbers = []
for i in range(0,25):
    y = random.randint(1,100)
    random_numbers.append(y)


input()
send("It was nice talking to you!")
input()
send(str(random_numbers))
input()
send(input('-> '))
input()
send(input('->'))
send(DISCONNECT_MESSAGE)
