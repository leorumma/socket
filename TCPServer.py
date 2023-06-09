import socket

# Lista de palavras disponíveis com suas respectivas traduções
palavras_disponiveis = {
    'protocolo': 'protocol',
    'roteador': 'router',
    'rede': 'network',
    'servidor': 'server',
    'cliente': 'client',
    'computador': 'computer',
    'porta': 'port',
    'conexão': 'connection',
    'atraso': 'delay'
}


# Função responsavel pelas traduções. Se a palavra não existir na lista eu retorno uma mensagem default.
def traduzir_palavras_para_ingles(palavra):
    return palavras_disponiveis.get(palavra, 'Palavra não encontrada no dicionário.')


def main():
    # Configurações do servidor
    HOST = 'localhost'
    PORT = 12003

    # Criação do socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket à uma porta
    server_socket.bind((HOST, PORT))

    # Define o limite de conexões pendentes
    server_socket.listen(1)
    print(f"Servidor TCP escutando na porta {PORT}")

    while True:
        # Esperando por uma conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        # Envia a lista de palavras disponíveis ao cliente
        palavras_disponiveis_str = ', '.join(palavras_disponiveis)
        client_socket.sendall(palavras_disponiveis_str.encode('utf-8'))

        while True:
            # Recebe a mensagem do cliente
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                break

            print(f"Palavra recebida: {data}")

            # Realiza a tradução
            resultado = traduzir_palavras_para_ingles(data)
            print(f"Tradução: {resultado}")

            # Envia a resposta ao cliente
            client_socket.sendall(resultado.encode('utf-8'))

        # Fecha o socket do cliente
        client_socket.close()
        print(f"Conexão com {client_address} finalizada")


if __name__ == '__main__':
    main()
