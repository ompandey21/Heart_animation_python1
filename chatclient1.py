import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
nickname = input('Choose a nickname: ')
def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print('Error occured')
            client.close()
            break

def write():
    while True:
        msg = f'{nickname}:{input("")}'
        client.send(msg.encode('utf-8'))

recieve_thread = threading.Thread(target= recieve)
recieve_thread.start()

write_thread = threading.Thread(target= write)
write_thread.start()

            