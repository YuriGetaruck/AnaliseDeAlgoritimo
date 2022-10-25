from dataclasses import dataclass
from turtle import distance
import pandas as pd
import numpy as np
import random


file = open('coordenadas.txt', 'r')

coordenadas_txt = file.readlines()


# print(coordenadas_txt)


coordenadas = np.arange(400, dtype=float).reshape(100, 4)

for i in range(100):
    coordenadas[i][0] = i
    coordenadas[i][1] = 0
    coordenadas[i][2] = 0
    coordenadas[i][3] = 0

# print(coordenadas_txt)

contador_linhas = 0

for line in coordenadas_txt:

    aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    contador = 0
    cont = 0
    for i in range(len(line)):

        if line[i] != (" "):
            #print('elemento = ' + str(line[i]) + '  Valor de i = ' +str(i) + ' Valor de aux-cont = '+str(i-cont))
            aux[i-cont] = line[i]
            #print('elemento = ' + line[i] + '  Valor de i = ' + str(i))
        else:
            cont = i+1
            contador += 1
            #print('elemento = ' + line[i] + '  Valor de i = ' +str(i) + ' Valor de aux-cont = '+str(i-cont))
            #print("contador = "+str(contador))
        if contador == 1:
            x_temp = float(''.join(aux))
            #print("x = "+str(x_temp))
            coordenadas[contador_linhas][1] = x_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
            #print("contador = "+str(contador))
            # print(aux)
        if contador == 3:
            y_temp = float(''.join(aux))
            #print("y = "+str(y_temp))
            coordenadas[contador_linhas][2] = y_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
            #print("contador = "+str(contador))
        if contador == 5:
            z_temp = float(''.join(aux))
            #print("z = "+str(z_temp))
            coordenadas[contador_linhas][3] = z_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
            #print("contador = "+str(contador))
    contador_linhas += 1


atual = 0
proximo = 0
distancia = 0

atual_coord = np.array([0, 0, 0], dtype=float)
proximo_coord = np.array([0, 0, 0], dtype=float)

posicao = np.arange(100)
posicao = np.delete(posicao, 0)

controle = True

while controle:

    posisao = random.shuffle(posicao)
    proximo = posicao[0]
    posicao = np.delete(posicao, 0)

    proximo_coord[0] = coordenadas[proximo][1]
    proximo_coord[1] = coordenadas[proximo][2]
    proximo_coord[2] = coordenadas[proximo][3]

    #print('coordenada atual')
    # print(atual_coord)
    #print('proxima coordenada')
    # print(proximo_coord)

    distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

    distancia += distancia_temp

    atual_coord[0] = proximo_coord[0]
    atual_coord[1] = proximo_coord[1]
    atual_coord[2] = proximo_coord[2]

    # print(distancia)

    if len(posicao.tolist()) == 0:
        controle = False


print('Distancia percorrida = ' + str(distancia))
