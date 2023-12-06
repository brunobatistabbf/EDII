import time

class No:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None
        self.altura = 1

def altura(no):
    if no is None:
        return 0
    return no.altura

def atualiza_altura(no):
    no.altura = 1 + max(altura(no.esquerda), altura(no.direita))

def rotacao_direita(z):
    y = z.esquerda
    T3 = y.direita

    y.direita = z
    z.esquerda = T3

    atualiza_altura(z)
    atualiza_altura(y)

    return y

def rotacao_esquerda(y):
    x = y.direita
    T2 = x.esquerda

    x.esquerda = y
    y.direita = T2

    atualiza_altura(y)
    atualiza_altura(x)

    return x

def rotacao_esquerda_direita(z):
    z.esquerda = rotacao_esquerda(z.esquerda)
    return rotacao_direita(z)

def rotacao_direita_esquerda(y):
    y.direita = rotacao_direita(y.direita)
    return rotacao_esquerda(y)

def fator_balanceamento(no):
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)

def inserir(raiz, data):
    if raiz is None:
        return No(data)

    if data < raiz.data:
        raiz.esquerda = inserir(raiz.esquerda, data)
    elif data > raiz.data:
        raiz.direita = inserir(raiz.direita, data)
    else:
        return raiz

    atualiza_altura(raiz)

    fator = fator_balanceamento(raiz)

    if fator > 1:
        if data < raiz.esquerda.data:
            return rotacao_direita(raiz)
        else:
            return rotacao_esquerda_direita(raiz)

    if fator < -1:
        if data > raiz.direita.data:
            return rotacao_esquerda(raiz)
        else:
            return rotacao_direita_esquerda(raiz)

    return raiz

def imprimir_em_ordem(raiz):
    if raiz:
        imprimir_em_ordem(raiz.esquerda)
        print(raiz.data, end=' ')
        imprimir_em_ordem(raiz.direita)

if __name__ == "__main__":
    # Leitura dos dados do arquivo e construção da árvore AVL
    with open('dados100_mil.txt', 'r') as arquivo:
        numeros = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]

    raiz = None
    inicio_tempo = time.time()

    for numero in numeros:
        raiz = inserir(raiz, numero)

    fim_tempo_insercao = time.time()
    tempo_insercao = fim_tempo_insercao - inicio_tempo
    print(f'Tempo de inserção: {tempo_insercao} segundos')

    # Impressão em ordem dos dados (comentado para economizar tempo de execução)
    inicio_tempo_impressao = time.time()
    imprimir_em_ordem(raiz)
    fim_tempo_impressao = time.time()
    tempo_impressao = fim_tempo_impressao - inicio_tempo_impressao
    print(f'\nTempo de impressão em ordem: {tempo_impressao} segundos')
