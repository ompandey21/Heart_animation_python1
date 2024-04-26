import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',9999))
server.listen()
clients = []
nicknames = []

def broadcast(msg):
   for client in clients:
        client.send(msg.encode('utf-8'))

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg.decode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f'{nicknames[index]} left the chat!')
            nicknames.remove(nicknames[index])
            break
        
def recieve():
    while True:
        client, addr = server.accept()
        print(f'connected with {str(addr)}')

        client.send('NICK'.encode('utf=8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!')
        client.send('Connected to the server'.encode('utf-8'))

        thread = threading.Thread(target= handle, args = (client,))
        thread.start()
print('Server is listening....')
recieve()

    



