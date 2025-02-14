import http.client
import threading
import time

def fazer_requisicao_get():
    # Conectar ao servidor localhost na porta 8000
    conexao = http.client.HTTPConnection("localhost", 8000)

    # Fazer a requisição GET
    conexao.request("GET", "/")

    # Obter a resposta
    resposta = conexao.getresponse()

    # Ler o conteúdo da resposta
    conteudo = resposta.read()

    # Imprimir o status e o conteúdo da resposta
    print(f"Status: {resposta.status}")
    print(f"Motivo: {resposta.reason}")
    print("Conteúdo:")
    print(conteudo.decode("utf-8"))

    # Fechar a conexão
    conexao.close()

# Chamar a função para fazer a requisição GET

def rodar_clientes(numero_de_clientes):
    threads = []

    # Criar threads para cada cliente
    for i in range(numero_de_clientes):
        t = threading.Thread(target=fazer_requisicao_get())
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    numero_de_clientes = int(input()) #colocar quantidade de clientes 
    start_time = time.time()
    rodar_clientes(numero_de_clientes)
    print(f"\nCom {numero_de_clientes} demorou: {time.time() - start_time}")