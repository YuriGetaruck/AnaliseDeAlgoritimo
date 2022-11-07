from dataclasses import dataclass
from turtle import distance
from unittest import skip
import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt

file = open('coordenadas.txt', 'r')

coordenadas_txt = file.readlines()

coordenadas = np.arange(400, dtype=float).reshape(100, 4)

for i in range(100):
    coordenadas[i][0] = i
    coordenadas[i][1] = 0
    coordenadas[i][2] = 0
    coordenadas[i][3] = 0

contador_linhas = 0

for line in coordenadas_txt:

    aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    contador = 0
    cont = 0
    for i in range(len(line)):

        if line[i] != (" "):
            aux[i-cont] = line[i]
        else:
            cont = i+1
            contador += 1
        if contador == 1:
            x_temp = float(''.join(aux))
            coordenadas[contador_linhas][1] = x_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
        if contador == 3:
            y_temp = float(''.join(aux))
            coordenadas[contador_linhas][2] = y_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1

        if contador == 5:
            z_temp = float(''.join(aux))
            coordenadas[contador_linhas][3] = z_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
    contador_linhas += 1


def randompath():

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

        distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

        distancia += distancia_temp

        atual_coord[0] = proximo_coord[0]
        atual_coord[1] = proximo_coord[1]
        atual_coord[2] = proximo_coord[2]

        if len(posicao.tolist()) == 0:
            controle = False

    return distancia


def inorderpath():  # parece errado

    proximo = 0
    distancia = 0

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    posicao = np.arange(100)
    posicao = np.delete(posicao, 0)

    controle = True

    distancias = np.arange(100, dtype=float)
    linha = 0

    while controle:

        proximo = posicao[0]
        posicao = np.delete(posicao, 0)

        proximo_coord[0] = coordenadas[proximo][1]
        proximo_coord[1] = coordenadas[proximo][2]
        proximo_coord[2] = coordenadas[proximo][3]

        distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

        distancias[linha] = distancia_temp

        distancia += distancia_temp

        atual_coord[0] = proximo_coord[0]
        atual_coord[1] = proximo_coord[1]
        atual_coord[2] = proximo_coord[2]

        if len(posicao.tolist()) == 0:
            controle = False
            distancia_temp = np.linalg.norm(atual_coord - [0, 0, 0])
            distancias[linha+1] = distancia_temp
            distancia += distancia_temp
        linha += 1

    print('Distancia percorrida InOrder= ' + str(distancia))


def closestpath():

    coordenadas_aux = np.delete(coordenadas, 0, 0)  # coordenadas sem o sol

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    caminho = np.zeros(101, dtype=int)
    caminho_aux = 1

    distancia_percorrida = 0

    controle = True

    range_for = 99

    while controle:

        distancias = np.ones(100)
        distancias = distancias*1000000

        for i in range(range_for):  # gera as distancias a partir do ponto atual

            proximo_coord[0] = coordenadas_aux[i][1]
            proximo_coord[1] = coordenadas_aux[i][2]
            proximo_coord[2] = coordenadas_aux[i][3]

            distancias[i] = np.linalg.norm(atual_coord - proximo_coord)

        # print(distancias)
        # print('------------------------------------------------------------------------------- ' +
        #       str(np.where(distancias == np.min(distancias))[0][0]))

        distancia_percorrida += np.min(distancias)

        posisao_no_vetor = (np.where(distancias == np.min(distancias))[0][0])

        caminho[caminho_aux] = coordenadas_aux[posisao_no_vetor][0]
        caminho_aux += 1

        atual_coord[0] = coordenadas_aux[posisao_no_vetor][1]
        atual_coord[1] = coordenadas_aux[posisao_no_vetor][2]
        atual_coord[2] = coordenadas_aux[posisao_no_vetor][3]

        coordenadas_aux = np.delete(coordenadas_aux, posisao_no_vetor, 0)

        # print(atual_coord)
        # print(distancia_percorrida)
        # print(coordenadas[posisao_no_vetor][0])

        range_for = range_for-1

        # if (range_for == 95):
        #     controle = False

        if (coordenadas_aux.shape[0] == 0):
            controle = False

    distancia_percorrida += np.linalg.norm(atual_coord - [0, 0, 0])

    print('Distancia Percorrida ClosestPath = '+str(distancia_percorrida))

    print(caminho)


def farestpath():

    coordenadas_aux = np.delete(coordenadas, 0, 0)  # coordenadas sem o sol

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    caminho = np.zeros(101, dtype=int)
    caminho_aux = 1

    distancia_percorrida = 0

    controle = True

    range_for = 99

    while controle:

        distancias = np.ones(100)
        distancias = distancias*1000000

        for i in range(range_for):  # gera as distancias a partir do ponto atual

            proximo_coord[0] = coordenadas_aux[i][1]
            proximo_coord[1] = coordenadas_aux[i][2]
            proximo_coord[2] = coordenadas_aux[i][3]

            distancias[i] = np.linalg.norm(atual_coord - proximo_coord)

        # print(distancias)
        # print('------------------------------------------------------------------------------- ' +
        #       str(np.where(distancias == np.min(distancias))[0][0]))

        distancia_percorrida += np.max(distancias)

        posisao_no_vetor = (np.where(distancias == np.min(distancias))[0][0])

        caminho[caminho_aux] = coordenadas_aux[posisao_no_vetor][0]
        caminho_aux += 1

        atual_coord[0] = coordenadas_aux[posisao_no_vetor][1]
        atual_coord[1] = coordenadas_aux[posisao_no_vetor][2]
        atual_coord[2] = coordenadas_aux[posisao_no_vetor][3]

        coordenadas_aux = np.delete(coordenadas_aux, posisao_no_vetor, 0)

        # print(atual_coord)
        # print(distancia_percorrida)
        # print(coordenadas[posisao_no_vetor][0])

        range_for = range_for-1

        # if (range_for == 95):
        #     controle = False

        if (coordenadas_aux.shape[0] == 0):
            controle = False

    distancia_percorrida += np.linalg.norm(atual_coord - [0, 0, 0])

    print('Distancia Percorrida ClosestPath = '+str(distancia_percorrida))

    print(caminho)


farestpath()

vetor = np.zeros(10000, dtype=float)
for i in range(10000):
    vetor[i] = randompath()

plt.figure()
plt.hist(vetor)
plt.show()


# fazer modelo 3D das rotas geradas
