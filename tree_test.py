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

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerda = self._remover(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            no.valor = self._menor_valor(no.direita)
            no.direita = self._remover(no.direita, no.valor)
        return no

    def _menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def preordem(self, no):
        if no:
            print(no.valor, end=' ')
            self.preordem(no.esquerda)
            self.preordem(no.direita)

    def inordem(self, no):
        if no:
            self.inordem(no.esquerda)
            print(no.valor, end=' ')
            self.inordem(no.direita)

    def posordem(self, no):
        if no:
            self.posordem(no.esquerda)
            self.posordem(no.direita)
            print(no.valor, end=' ')

    def em_nivel(self):
        if not self.raiz:
            return

        fila = [self.raiz]
        while fila:
            no = fila.pop(0)
            print(no.valor, end=' ')
            if no.esquerda:
                fila.append(no.esquerda)
            if no.direita:
                fila.append(no.direita)


# Função para sortear 20 números de 0 a 100
import random
numeros = random.sample(range(101), 20)

# Criar e preencher a árvore
arvore = ArvoreBinaria()
for numero in numeros:
    arvore.inserir(numero)

# Imprimir pré-ordem, in-ordem, pós-ordem e em nível
print("Árvore original:")
print("Pré-ordem:", end=' ')
arvore.preordem(arvore.raiz)
print("\nIn-ordem:", end=' ')
arvore.inordem(arvore.raiz)
print("\nPós-ordem:", end=' ')
arvore.posordem(arvore.raiz)
print("\nEm nível:", end=' ')
arvore.em_nivel()

# Remover 5 elementos
elementos_a_remover = random.sample(numeros, 5)
for elemento in elementos_a_remover:
    arvore.remover(elemento)

# Imprimir novamente após a remoção
print("\n\nÁrvore após remoção de 5 elementos:")
print("Pré-ordem:", end=' ')
arvore.preordem(arvore.raiz)
print("\nIn-ordem:", end=' ')
arvore.inordem(arvore.raiz)
print("\nPós-ordem:", end=' ')
arvore.posordem(arvore.raiz)
print("\nEm nível:", end=' ')
arvore.em_nivel()
