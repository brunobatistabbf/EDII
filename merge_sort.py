import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [int(line.strip()) for line in file]

    return data

if __name__ == "__main__":
    with open('dados100_mil.txt', 'r') as arquivo:
        numeros = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]

    start_time = time.time()
    sorted_data = merge_sort(numeros)
    end_time = time.time()

    print("Dados ordenados usando Insertion Sort:")
    for numero in sorted_data:
        print(numero, end=' ')
    print("\nTempo de execução para ordenar o arquivo: {:.6f} segundos".format(end_time - start_time))

    # Imprimir os dados ordenados (opcional)
    # print("Dados ordenados:", sorted_data)
