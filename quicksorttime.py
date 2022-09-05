import numpy as np
import time
import matplotlib.pyplot as plt

resultado_pior = np.arange(0,10,dtype=float)
resultado_medio = np.arange(0,10,dtype=float)
resultado_melhor = np.arange(0,10,dtype=float)

arq_result =  open('resultados_quick_10000', 'w+')

resultados = np.arange(0,10,dtype=float)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    
def teste_medio(tamanho_vetor):
    for i in range(10):
        begin =  time.time()
        vetor = np.random.randint(0,1000, tamanho_vetor)
        quick_sort(vetor,0,len(vetor)-1)
        end =  time.time()
        resultados[i]=end-begin

teste_medio(100000)

arq_result.close()

print(resultados)
