# uab-redes
Repositório público para utilização na disciplina de Redes de Computadores - UFR-UaB


# 💻 Comunicação TCP e UDP (Python e Java)

Este repositório contém exemplos simples de **comunicação entre cliente e servidor** usando os protocolos **TCP** e **UDP**, nas linguagens **Python** e **Java**.  
Os exemplos fazem parte das atividades práticas da disciplina **Redes de Computadores** (Unidade III).

---

## 🎯 Objetivo

Demonstrar, na prática, como ocorre o envio e recebimento de mensagens em redes:
- **TCP (Transmission Control Protocol):** orientado à conexão, confiável e com controle de fluxo.  
- **UDP (User Datagram Protocol):** não orientado à conexão, rápido, mas sem garantias de entrega.

---

## ⚙️ Como executar

### ▶️ Em Python
1. Abra dois terminais.
2. No primeiro, execute o servidor:
   ```bash
   python tcp_server.py

   python tcp_client.py

### ▶️ Em Java
1. Compile os arquivos de código fonte:
   ```bash
   javac ServidorTCPBasico.java ClienteTCPBasico.java RemetenteUDP.java ReceptorUDP.java

2. Exemplo de execução:
   ```bash
   java ServidorTCPBasico
   java ClienteTCPBasico


