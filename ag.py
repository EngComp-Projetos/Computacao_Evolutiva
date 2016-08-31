from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt
import csv

numcolunas = 3 #Numero de colunas da matriz
numlinhas = 3 #Num de linhas da Matriz
numeroindividuos = 3

def criarpop(): 
    populacao = np.zeros((numeroindividuos, numlinhas, numcolunas))
    # print(populacao)
    print(populacao[0][0][0])

def fitness():
    pass

criarpop()