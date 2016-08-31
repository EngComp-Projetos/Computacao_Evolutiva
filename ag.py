# coding=UTF-8

import numpy as np
# from random import randint, uniform
# import matplotlib.pyplot as plt
# import csv

numcolunas = 3  # Número de colunas da matriz
numlinhas = 3  # Número de linhas da matriz
numerotrilhas = 3  # Quantidade de trilhas na placa
populacao = []
tamanhopopulacao = 50


def criarpop(): 
    for i in range(0, tamanhopopulacao):
        populacao.append(geraindividuos())
    print(populacao[0])


def geraindividuos():
    individuo = np.zeros((numerotrilhas, numlinhas, numcolunas))
    # print(individuo)
    # print(individuo[0][0][0])

    return individuo


def fitness():
    pass


criarpop()
