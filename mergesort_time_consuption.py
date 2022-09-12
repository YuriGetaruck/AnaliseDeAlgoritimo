import numpy as np
import time
import matplotlib.pyplot as plt


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


resultado_pior = np.arange(0, 10, dtype=float)
resultado_medio = np.arange(0, 10, dtype=float)
resultado_melhor = np.arange(0, 10, dtype=float)

arq_result = open('resultados_merge_1000', 'w+')


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


tamanhovetor = 10000


arq_result.write("--------------MELHOR CASO--------------\n")
print("Iniciando melhor caso")
teste_melhor(tamanhovetor)
arq_result.write("--------------CASO MEDIO--------------\n")
print("iniciando caso medio")
teste_medio(tamanhovetor)
arq_result.write("--------------PIOR CASO--------------\n")
print("iniciando pior caso")
teste_pior(tamanhovetor)

arq_result.close()


plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.stem(resultado_melhor)
# plt.axis([0,11,0,0.3])
plt.subplot(132)
plt.stem(resultado_medio)
# plt.axis([0,11,0,0.3])
plt.subplot(133)
plt.stem(resultado_pior)
# plt.axis([0,11,0,0.3])
plt.show()

plt.figure()
plt.plot([np.mean(resultado_melhor), np.mean(
    resultado_medio), np.mean(resultado_pior)])
