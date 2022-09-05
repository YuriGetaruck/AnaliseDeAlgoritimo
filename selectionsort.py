import numpy as np
import time



arq_result =  open('resultados_100000', 'w+')

def insertionSort(vetor):
    cont=0
    for i in range(1, len(vetor)):
        
        key = vetor[i]
        cont+=1
        j = i - 1
        cont+=3
        while j >= 0 and key < vetor[j]:
            cont+=1
            vetor[j + 1] = vetor[j]
            cont+=1
            j = j - 1
            cont+=2
            
        vetor[j + 1] = key
        cont+=1
    return cont


def teste_medio(tamanho_vetor):
    for times in range(10):

        
        begin = time.time()
        vetor = np.random.randint(0,1000,tamanho_vetor)
        #print("\nVetor antes:")
        ##    print(str(vetor[i]),end=" ")
        #print("\n")
        cont = insertionSort(vetor)
        #print('Vetor organizado em ordem crescente:')
        #for i in range(len(vetor)):
        #    print(str(vetor[i]),end=" ")
        end = time.time()
        arq_result.write("Tempo de execucao: "+ str(end-begin) + "sec." +"\nNumero de interacoes: "+str(cont)+ "\n\n")

def teste_pior(tamanho_vetor):
    for times in range(10):

        
        begin = time.time()
        vetor = np.arange(0,tamanho_vetor)
        for i in range(len(vetor)):
            i+=1
            vetor[tamanho_vetor-i] = i
        #print("\nVetor antes:")
        #for i in range(len(vetor)):
        #    print(str(vetor[i]),end=" ")
        #print("\n")
        cont = insertionSort(vetor)
        #print('\nNumero de interacoes: '+str(cont))
        #print('Vetor organizado em ordem crescente:')
        #for i in range(len(vetor)):
        #    print(str(vetor[i]),end=" ")
        end = time.time()
        arq_result.write("Tempo de execucao: "+ str(end-begin) + "sec." +"\nNumero de interacoes: "+str(cont)+ "\n\n")

def teste_melhor(tamanho_vetor):
    for times in range(10):

        
        begin = time.time()
        vetor = np.ones((tamanho_vetor,), dtype=int)
        for i in range(tamanho_vetor):
            vetor[i] = i
        #print("\nVetor antes:")
        #for i in range(len(vetor)):
        #    print(str(vetor[i]),end=" ")
        #print("\n")
        cont = insertionSort(vetor)
        #print('\nNumero de interacoes: '+str(cont))
        #print('Vetor organizado em ordem crescente:')
        #for i in range(len(vetor)):
        #    print(str(vetor[i]),end=" ")
        end = time.time()
        arq_result.write("Tempo de execucao: "+ str(end-begin) + "sec." +"\nNumero de interacoes: "+str(cont)+ "\n\n")

tamanhovetor = 100000
arq_result.write("--------------MELHOR CASO--------------\n")
teste_melhor(tamanhovetor)
arq_result.write("--------------CASO MEDIO--------------\n")
teste_medio(tamanhovetor)
arq_result.write("--------------PIOR CASO--------------\n")
teste_pior(tamanhovetor)



arq_result.close()

#Para o pior caso o numero de interações será N^2
#Para o caso médio o numero de intrrações será N^2
#Para o melhor caso o numero de interações será N
