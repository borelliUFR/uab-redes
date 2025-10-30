import socket

HOST = '127.0.0.1'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"Servidor UDP aguardando mensagens em {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    print(f"Recebido de {addr}: {data.decode()}")
    server.sendto(b"Mensagem recebida via UDP!", addr)