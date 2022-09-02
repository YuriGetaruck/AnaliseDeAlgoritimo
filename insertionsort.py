import numpy as np


def insertionSort(array):

    contador = 0

    for i in range(1, len(array)):
        key = array[i]
        contador+=1
        j = i - 1
        contador+=1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            contador+=1
            j = j - 1
            contador+=1
        
        array[j + 1] = key
        contador+=1
    print('Numero de interacoes: '+str(contador))


vetor = np.random.randint(0,100,100000)
insertionSort(vetor)
print('Vetor organizado em ordem crescente:')
for i in range(len(vetor)):
    print(str(vetor[i]),end=" ")

#Para o pior caso o numero de interações será N^2
#Para o caso médio o numero de intrrações será N^2
#Para o melhor caso o numero de interações será N

