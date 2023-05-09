import socket

def main():
    # Configurações do cliente
    HOST = 'localhost'
    PORT = 12003

    # Criação do socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexão com o servidor
    client_socket.connect((HOST, PORT))

    # Recebe a lista de palavras disponíveis
    lista_palavras = client_socket.recv(1024).decode('utf-8')
    print(f"Palavras disponíveis: {lista_palavras}")

    while True:
        # Solicita a palavra a ser traduzida
        palavra = input("Digite a palavra a ser traduzida (ou 'sair' para encerrar conexão): ")

        if palavra == 'sair':
            break

        # Envia a palavra ao servidor
        client_socket.sendall(palavra.encode('utf-8'))

        # Recebe a tradução do servidor
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Tradução: {data}")

    # Encerra a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    main()
