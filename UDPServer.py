import socket

def traduzir(palavra):
    if palavra == 'casa':
        return 'house'
    elif palavra == 'carro':
        return 'car'
    elif palavra == 'escola':
        return 'school'
    elif palavra == 'trabalho':
        return 'work'
    elif palavra == 'telefone':
        return 'phone'
    elif palavra == 'computador':
        return 'computer'
    elif palavra == 'música':
        return 'music'
    elif palavra == 'livro':
        return 'book'
    elif palavra == 'tempo':
        return 'time'
    else:
        return 'Palavra não encontrada no dicionário.'

def main():
    servidor_ip = '127.0.0.1'
    servidor_porta = 12000

    # Cria o socket do servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Associa o socket do servidor ao IP e porta
    servidor_socket.bind((servidor_ip, servidor_porta))

    print(f'Servidor UDP rodando em {servidor_ip}:{servidor_porta}...')
    while True:
        # Recebe a palavra do cliente
        data, cliente_endereco = servidor_socket.recvfrom(1024)

        # Decodifica a palavra recebida
        palavra = data.decode()

        if palavra.lower() == 'sair':
            break

        # Traduz a palavra
        traducao = traduzir(palavra.lower())

        # Envia a tradução para o cliente
        servidor_socket.sendto(traducao.encode(), cliente_endereco)

    # Fecha o socket do servidor
    servidor_socket.close()

if __name__ == '__main__':
    main()
