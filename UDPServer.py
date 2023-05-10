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

def traduzir_palavras_para_ingles(palavra):
    return palavras_disponiveis.get(palavra, 'Palavra não encontrada no dicionário.')

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
        traducao = traduzir_palavras_para_ingles(palavra.lower())

        # Envia a tradução para o cliente
        servidor_socket.sendto(traducao.encode(), cliente_endereco)

    # Fecha o socket do servidor
    servidor_socket.close()

if __name__ == '__main__':
    main()
