import socket


def main():
    servidor_ip = '127.0.0.1'
    servidor_porta = 12000

    # Cria o socket do cliente
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('Digite a palavra a ser traduzida ou digite "sair" para encerrar.')
    while True:
        # Recebe a palavra do usuário
        palavra = input('> ')

        if palavra.lower() == 'sair':
            break

        # Envia a palavra para o servidor
        cliente_socket.sendto(palavra.encode(), (servidor_ip, servidor_porta))

        # Recebe a resposta do servidor
        data, _ = cliente_socket.recvfrom(1024)

        # Exibe a resposta do servidor
        print(f'Tradução: {data.decode()}')

    # Fecha o socket do cliente
    cliente_socket.close()


if __name__ == '__main__':
    main()
