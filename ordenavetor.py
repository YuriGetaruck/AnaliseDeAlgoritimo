import time
import numpy as np

tamanho_vetor = 100000000

resultado = np.arange(0,10, dtype=float)


for i in range(10):
    begin = time.time()
    vetor = np.random.randint(0,1000,tamanho_vetor)
    np.sort(vetor)
    end = time.time()
    resultado[i] = end - begin
    print(resultado)

print(resultado)
