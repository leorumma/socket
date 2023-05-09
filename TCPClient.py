import socket

def main():
    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Endereço IP e Porta do servidor
    server_address = ('localhost', 12001)

    # Conecta ao servidor
    client_socket.connect(server_address)

    # Recebe a lista de palavras disponíveis do servidor
    data = client_socket.recv(1024).decode()
    print('Palavras disponíveis:', data)

    # Loop principal para a tradução de palavras
    while True:
        # Lê a palavra do usuário
        palavra = input('Digite uma palavra para traduzir ou "sair" para encerrar: ').lower()

        # Encerra o loop se o usuário digitar "sair"
        if palavra == 'sair':
            break

        # Envia a palavra ao servidor
        client_socket.sendall(palavra.encode())

        # Recebe a resposta do servidor
        data = client_socket.recv(1024).decode()

        # Exibe a resposta
        print('Tradução:', data)

    # Fecha o socket
    client_socket.close()

if __name__ == '__main__':
    main()
