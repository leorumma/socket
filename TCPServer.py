import socket


def traduzir(palavra):
    dicionario = {
        'casa': 'house',
        'carro': 'car',
        'escola': 'school',
        'trabalho': 'work',
        'telefone': 'phone',
        'computador': 'computer',
        'música': 'music',
        'livro': 'book',
        'tempo': 'time'
    }
    return dicionario.get(palavra, 'Palavra não encontrada no dicionário.')


def main():
    # Configurações do servidor
    HOST = 'localhost'
    PORT = 12001

    # Criação do socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen(1)
    print(f"Servidor TCP escutando na porta {PORT}")

    while True:
        # Esperando por uma conexão
        cliente_socket, cliente_endereco = servidor_socket.accept()
        print(f"Conexão estabelecida com {cliente_endereco}")

        while True:
            # Recebe a mensagem do cliente
            data = cliente_socket.recv(1024).decode('utf-8')

            if not data:
                break

            print(f"Palavra recebida: {data}")

            # Realiza a tradução
            resultado = traduzir(data)
            print(f"Tradução: {resultado}")

            # Envia a resposta ao cliente
            cliente_socket.sendall(resultado.encode('utf-8'))

        # Fecha o socket do cliente
        cliente_socket.close()
        print(f"Conexão com {cliente_endereco} finalizada")


if __name__ == '__main__':
    main()
