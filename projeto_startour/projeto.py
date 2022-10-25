from dataclasses import dataclass
import pandas
import numpy as np


file = open('coordenadas.txt', 'r')

coordenadas_txt = file.readlines()


# print(coordenadas_txt)


coordenadas = np.arange(400).reshape(100, 4)


for line in coordenadas_txt:

    aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    contador = 0
    #line = line.replace(".", ",")

    for i in range(len(line)):

        if line[i] != " ":
            aux[i] = line[i]
        else:
            contador += 1
            print("contador = "+str(contador))
        if contador == 1:
            x_temp = float(''.join(aux))
            print("x = "+str(x_temp))
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
        if contador == 2:
            y_temp = float(''.join(aux))
            print(y_temp)
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
        if contador == 3:
            z_temp = float(''.join(aux))
            print(z_temp)
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])


for i in range(100):
    coordenadas[i][0] = i
    coordenadas[i][1] = 0
    coordenadas[i][2] = 0
    coordenadas[i][3] = 0

# print(coordenadas)

# print(coordenadas_txt)
