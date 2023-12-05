import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def main():
    # Leitura dos dados do arquivo
    with open('dados100_mil.txt', 'r') as arquivo:
        numeros = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]

    # Copiando a lista para preservar a original (Insertion Sort é in-place)
    numeros_insertion_sort = numeros.copy()

    inicio_insertion_sort = time.time()

    insertion_sort(numeros_insertion_sort)

    tempo_insertion_sort = time.time() - inicio_insertion_sort

    # Imprimindo os dados ordenados
    print("Dados ordenados usando Insertion Sort:")
    for numero in numeros_insertion_sort:
        print(numero, end=' ')
    print("\n\nTempo de execução do Insertion Sort:", tempo_insertion_sort, "segundos")

if __name__ == "__main__":
    main()
