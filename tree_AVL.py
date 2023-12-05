import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVLTree:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        if not no:
            return 0
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def rotacao_direita(self, z):
        y = z.esquerda
        T2 = y.direita

        y.direita = z
        z.esquerda = T2

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def rotacao_esquerda(self, y):
        x = y.direita
        T2 = x.esquerda

        x.esquerda = y
        y.direita = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, no, valor):
        if not no:
            return No(valor)

        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.inserir(no.direita, valor)
        else:
            return no  # Ignorar duplicatas

        self.atualizar_altura(no)

        balanceamento = self.fator_balanceamento(no)

        # Casos de desbalanceamento
        if balanceamento > 1:
            if valor < no.esquerda.valor:
                return self.rotacao_direita(no)
            else:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
                return self.rotacao_direita(no)

        if balanceamento < -1:
            if valor > no.direita.valor:
                return self.rotacao_esquerda(no)
            else:
                no.direita = self.rotacao_direita(no.direita)
                return self.rotacao_esquerda(no)

        return no

    def imprimir_inordem(self, no):
        if no:
            self.imprimir_inordem(no.esquerda)
            print(no.valor, end=' ')
            self.imprimir_inordem(no.direita)

def inserir_avl(arvore, numeros):
    for numero in numeros:
        arvore.raiz = arvore.inserir(arvore.raiz, numero)

def main():
    arvore_avl = AVLTree()

    # Leitura dos dados do arquivo
    with open('dados100_mil.txt', 'r') as arquivo:
        numeros = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]

    inicio_total = time.time()

    inicio_insercao_avl = time.time()
    inserir_avl(arvore_avl, numeros)
    tempo_insercao_avl = time.time() - inicio_insercao_avl

    inicio_impressao_avl = time.time()
    arvore_avl.imprimir_inordem(arvore_avl.raiz)
    tempo_impressao_avl = time.time() - inicio_impressao_avl

    tempo_total = time.time() - inicio_total

    print("\n\nTempo de inserção com AVL:", tempo_insercao_avl, "segundos")
    print("Tempo de impressão com AVL:", tempo_impressao_avl, "segundos")
    print("Tempo total de execução:", tempo_total, "segundos")

if __name__ == "__main__":
    main()

