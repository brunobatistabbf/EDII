import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)
        return no

    def em_ordem(self, no, lista):
        if no:
            self.em_ordem(no.esquerda, lista)
            lista.append(no.valor)
            self.em_ordem(no.direita, lista)

    def construir_lista_dsw(self):
        lista = []
        self.em_ordem(self.raiz, lista)
        return lista

    def balancear_dsw(self):
        lista = self.construir_lista_dsw()
        n = len(lista)

        m = 2**(n.bit_length()) - 1
        self.raiz = self._balancear_dsw(lista, m, n)

    def _balancear_dsw(self, lista, m, n):
        raiz = No(None)
        raiz.direita = self._linearizar(lista, m, n)
        self._otimizar(raiz, n)
        return raiz.direita

    def _linearizar(self, lista, m, n):
        raiz = No(None)
        p = raiz
        i = 0

        while i < n:
            filho = No(lista[i])
            p.direita = filho
            p = filho
            i += 1

            for j in range(1, m):
                if i < n:
                    filho.direita = No(lista[i])
                    filho = filho.direita
                    i += 1

        return raiz.direita

    def _otimizar(self, raiz, n):
        m = 2**(n.bit_length()) - 1
        p = raiz
        q = p.direita

        for i in range(n - m):
            r = q.direita
            if r:
                q.direita = r.direita
                r.direita = p.direita
                p.direita = r
                p = r
                q = p.direita
            else:
                break

    def imprimir_inordem(self, no):
        if no:
            self.imprimir_inordem(no.esquerda)
            print(no.valor, end=' ')
            self.imprimir_inordem(no.direita)

# Cria arvore com 100 números
arvore = ArvoreBinaria()
numeros = random.sample(range(101), 100)

for numero in numeros:
    arvore.inserir(numero)

# Imprimi árvore
print("Árvore antes do balanceamento:")
arvore.imprimir_inordem(arvore.raiz)
print("\n")

# Algoritmo DSW
arvore.balancear_dsw()

# Imprimir balanceamento
print("Árvore após o balanceamento:")
arvore.imprimir_inordem(arvore.raiz)
print("\n")

# Acrescentar 20 números
novos_numeros = random.sample(range(101, 201), 20)

for novo_numero in novos_numeros:
    arvore.inserir(novo_numero)

# Imprimir  20 números
print("Árvore após a adição de 20 números:")
arvore.imprimir_inordem(arvore.raiz)
print("\n")

# Implementar o Algoritmo DSW denovo
arvore.balancear_dsw()

# Segundo balanceamento
print("Árvore após o segundo balanceamento:")
arvore.imprimir_inordem(arvore.raiz)
print("\n")
