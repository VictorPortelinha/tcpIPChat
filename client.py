import socket
import threading
import time

nickname = input("Escolha um apelido: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',5550))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii') # recebe mensagens do client
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Um erro ocorreu")
            client.close()

def write():
    while True:
        try:
            time.sleep(1.5)
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))
        except:
            print("Um erro ocorreu")
            client.close()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()