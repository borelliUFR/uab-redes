import socket

HOST = 'localhost'   # Endereço local
PORT = 1000          # Porta do servidor

# Cria o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor TCP escutando em {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Recebido: {data.decode()}")
    conn.sendall(b"Mensagem recebida pelo servidor!")

conn.close()
server.close()