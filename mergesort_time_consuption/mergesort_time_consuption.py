import numpy as np
import time
import matplotlib.pyplot as plt


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def teste_medio(tamanho_vetor):
    for times in range(10):
        vetor = np.random.randint(0, 1000, tamanho_vetor)
        inicio = 0
        fim = tamanho_vetor-1
        begin = time.time()
        mergeSort(vetor, inicio, fim)
        end = time.time()
        resultado_medio[times] = end-begin
        arq_result.write("Tempo de execucao: " + str(end-begin) + "sec.\n")


def teste_pior(tamanho_vetor):
    for times in range(10):
        vetor = np.arange(tamanho_vetor, 0, -1)
        inicio = 0
        fim = tamanho_vetor-1
        begin = time.time()
        mergeSort(vetor, inicio, fim)
        end = time.time()
        resultado_pior[times] = end-begin
        arq_result.write("Tempo de execucao: " + str(end-begin) + "sec.\n")


def teste_melhor(tamanho_vetor):
    for times in range(10):

        vetor = np.arange(0, tamanho_vetor)
        vetor_inicio = 0
        vetor_fim = tamanho_vetor-1
        begin = time.time()
        mergeSort(vetor, vetor_inicio, vetor_fim)
        end = time.time()
        resultado_melhor[times] = end-begin
        arq_result.write("Tempo de execucao: " + str(end-begin) + "sec.\n")


resultado_pior = np.arange(0, 10, dtype=float)
resultado_medio = np.arange(0, 10, dtype=float)
resultado_melhor = np.arange(0, 10, dtype=float)

arq_result = open('resultados_merge_1000', 'w+')


tamanhos = [10000, 25000, 50000, 100000, 200000]

medias_pior = np.arange(0, 5, dtype=float)
medias_medio = np.arange(0, 5, dtype=float)
medias_melhor = np.arange(0, 5, dtype=float)

for i in range(5):

    arq_result.write("Tamanho do vetor: " + str(tamanhos[i]) + "--->\n")
    arq_result.write("--------------MELHOR CASO--------------\n")
    print("Iniciando melhor caso")
    teste_melhor(tamanhos[i])
    arq_result.write("--------------CASO MEDIO--------------\n")
    print("iniciando caso medio")
    teste_medio(tamanhos[i])
    arq_result.write("--------------PIOR CASO--------------\n")
    print("iniciando pior caso")
    teste_pior(tamanhos[i])
    medias_melhor[i] = np.mean(resultado_melhor)
    medias_medio[i] = np.mean(resultado_medio)
    medias_pior[i] = np.mean(resultado_pior)

arq_result.close()


plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo consumido em segundos")
plt.plot(["10000", "25000", "50000", "100000", "200000"], medias_melhor)

plt.subplot(132)
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo consumido em segundos")
plt.plot(["10000", "25000", "50000", "100000", "200000"], medias_medio)

plt.subplot(133)
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo consumido em segundos")
plt.plot(["10000", "25000", "50000", "100000", "200000"], medias_pior)

plt.suptitle("Grafico com as médias dos tempos de execucao")
plt.show()
