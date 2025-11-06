import socket

HOST = "127.0.0.1"   # Escuta em todas as interfaces de rede
PORT = 8080        # Porta HTTP alternativa (80 geralmente exige privilégio)

# Cria socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite reutilizar a porta rapidamente após encerrar o programa
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o socket ao endereço e porta
server.bind((HOST, PORT))

# Coloca o socket em modo de escuta (fila de até 5 conexões pendentes)
server.listen(5)
print(f"Servidor Web simples ouvindo em http://localhost:{PORT}/")

while True:
    # Aceita uma nova conexão
    conn, addr = server.accept()
    print(f"Conexão de: {addr}")

    # Recebe os dados enviados pelo cliente (navegador)
    request = conn.recv(1024).decode("utf-8", errors="ignore")
    print("===== Requisição recebida =====")
    print(request)
    print("===============================")

    # Monta uma resposta HTTP simples
    body = """
    <html>
      <head><title>Servidor Web Simples</title></head>
      <body>
        <h1>Olá, mundo da rede!</h1>
        <p>Este é um servidor Web desenvolvido em Python.</p>
        <p>Camada de Aplicação: HTTP | Camada de Transporte: TCP</p>

      </body>
    </html>
    """

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode('utf-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )

    # Envia a resposta para o cliente
    conn.sendall(response.encode("utf-8"))

    # Encerra a conexão
    conn.close()