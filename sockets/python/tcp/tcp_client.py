import socket

HOST = '127.0.0.1'  # Mesmo endereço do servidor
PORT = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = input("Digite a mensagem: ")
client.sendall(msg.encode())

data = client.recv(1024)
print("Resposta do servidor:", data.decode())

client.close()