import numpy as np
from random import randint, uniform
import time
import csv

tamanho_populacao = 50
taxa_cruzamento = 75
taxa_mutacao = 1
geracoes = 100
geracao_atual = 0
matriz_referencia = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 9, 0, 0],
                     [0, 0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 2, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 5, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def cria_populacao(tamanho_populacao, referencia):
    populacao = []
    for k in range(0, tamanho_populacao):
        individuo = np.zeros((9, 9))
        for j in range(0, 9):  # coluna
            for i in range(0, 9):  # linha
                refe = referencia[i][j]
                if refe == 0:
                    individuo[i][j] = randint(1, 9)
                else:
                    individuo[i][j] = referencia[i][j]
        populacao.append(individuo)
    return populacao


def fitness(populacao):
    """
    Esta função calculará a fitness de cada candidata a solução da seguinte forma:
    O valor inicial de fitness será zero (valor máximo)
    A cada desvio da regra detectado (repetição de número no quadrante, coluna ou linha)
    O valor de fitness será decrescido de 1
    """
    vetor_fitness = np.zeros(50)
    for k in range(0, 50):
        for j in range(0, 9):  # Verificar repeticao na coluna
            repeticao = []
            for i in range(0, 9):
                valor = populacao[k][i][j]
                for va in range(0, len(repeticao)):
                    if valor == repeticao[va]:
                        vetor_fitness[k] -= 1
                        break
                repeticao.append(valor)
        for i in range(0, 9):  # Verificar repeticao na linha
            repeticao = []
            for j in range(0, 9):
                valor = populacao[k][i][j]
                for va in range(0, len(repeticao)):
                    if valor == repeticao[va]:
                        vetor_fitness[k] -= 1
                        break
                repeticao.append(valor)
        # Os loops a seguir farão a varredura dos quadrantes do tabuleiro em busca de repetição dos números
        j, i, w, l = 0, 0, 0, 0
        while j < 9:
            while i < 9:
                repeticao = []
                while w < 3:
                    while l < 3:
                        valor = populacao[k][i + w][j + l]
                        for va in range(0, len(repeticao)):
                            if valor == repeticao[va]:
                                vetor_fitness[k] -= 1
                                break
                        repeticao.append(valor)
                        l += 1
                    l = 0
                    w += 1
                w = 0
                i += 3
            i = 0
            j += 3
    print(len(vetor_fitness))
    print(vetor_fitness)
    return vetor_fitness


def selecao(populacao, vetor_aptidao):  # Esta funcao selecionara um individuo utilizando o metodo da roleta
    soma, acumulador, ind = 0, vetor_aptidao[0], 0
    selecionado = []
    soma = sum(vetor_aptidao)
    num_aleatorio = uniform(0, soma)
    while len(selecionado) != 2:
        acumulador += vetor_aptidao[ind]
        if acumulador <= num_aleatorio:
            selecionado = populacao[ind]
            break
        ind += 1
    return selecionado


def mais_apto(aptidoes, populacao):
    # Esta função retorna a maior aptidão e o cromossomo do indivíduo com a maior aptidão
    apto = aptidoes[0]
    cromossomo = populacao[0]
    for i in range(1, len(aptidoes)):
        if apto < aptidoes[i]:
            apto = aptidoes[i]
            cromossomo = populacao[i]

    return apto, cromossomo


def cruzamento(populacao_1, populacao_2, aptidao_cruzamento):
    contador = 0
    while contador < tamanho_popula:
        vetor = selecao(populacao_1, aptidao_cruzamento)
        pai_1 = vetor
        vetor = selecao(populacao_1, aptidao_cruzamento)
        pai_2 = vetor
        aleatorio = uniform(0, 100)
        if aleatorio < taxa_cruzamento:
            populacao_2 = aritmetico(pai_1, pai_2, populacao_2)
            contador += 2
    return populacao_2


def aritmetico(pai_1, pai_2, populacao):
    # Implemntação do cruzamento aritmético
    # a - número aleatório entre 0 e 1
    # F1 = (a * p1) + ((1 - a) * p2) e F2 = (a * p2) + ((1 - a) * p1)
    a = uniform(0, 1)
    filho1 = np.zeros((9, 9))
    filho2 = np.zeros((9, 9))
    for j in range(0, 9):
        for i in range(0, 9):
            filho1[i][j] = int((a * pai_1[i][j]) + ((1 - a) * pai_2[i][j]))
            filho2[i][j] = int((a * pai_2[i][j]) + ((1 - a) * pai_1[i][j]))
    populacao.append(filho1)
    populacao.append(filho2)
    return populacao


def mutacao(popatual, txmutacao):
    popmutada = []
    for i in range(0, len(popatual)):
        individuo = popatual[i]
        for k in range(0, 9):
            for j in range(0, 9):
                ponto = randint(0,100)
                if ponto <= txmutacao:
                    individuo[j][k] = randint(1,9)
        popmutada.append(individuo)
    return popmutada


def elitismo(populacao_apto, aptidoes, populacao):
    global tamanho_populacao_cruzamento
    maior_apitdao, melhor_cromossomo = mais_apto(aptidoes, populacao_apto)
    if tamanho_populacao == tamanho_populacao_cruzamento:
        populacao.append(melhor_cromossomo)
        tamanho_populacao_cruzamento += 1
    else:
        populacao.append(melhor_cromossomo)
    return populacao


def heap_sort(lista, cromossomo):
    indice_final = len(lista) - 1
    metade_lista = int(indice_final / 2)

    for i in range(metade_lista, -1, -1):
        cria_heap(lista, cromossomo, i, indice_final)

    for i in range(indice_final, 0, -1):
        if lista[0] > lista[i]:
            lista[0], lista[i] = lista[i], lista[0]
            cromossomo[0], cromossomo[i] = cromossomo[i], cromossomo[0]
            cria_heap(lista, cromossomo, 0, i - 1)
    return lista, cromossomo


def cria_heap(lista, cromossomo, inicio, fim):
    filho = inicio * 2 + 1
    while filho <= fim:
        if (filho < fim) and (lista[filho] < lista[filho + 1]):
            filho += 1
        if lista[inicio] < lista[filho]:
            lista[inicio], lista[filho] = lista[filho], lista[inicio]
            cromossomo[inicio], cromossomo[filho] = cromossomo[filho], cromossomo[inicio]
            inicio = filho
            filho = 2 * inicio + 1
        else:
            return


def normalizacao_linear(tamanho_populacao, minimo=10, maximo=100):
    aptidao_normalizada = []
    for i in range(0, tamanho_populacao):
        normalizada = minimo + (((maximo - minimo)/(tamanho_populacao - 1)) * i)
        aptidao_normalizada.append(normalizada)
    return aptidao_normalizada

# c = csv.writer(open('aptos_real.csv', 'w'))
# d = csv.writer(open('media_real.csv', 'w'))
# r = csv.writer(open('piores_individuos_real.csv', 'w'))
for var1 in range(0, 10):
    populacao_nova = cria_populacao(tamanho_populacao, matriz_referencia)
    var = 0
    while var < 3:
        print(var)
        aptos = []
        media_apt = []
        pior_individuo = []
        popula = populacao_nova
        while geracao_atual < geracoes:
            aptidao = fitness(popula)
            
            popula = normalizacao_linear(tamanho_populacao)
            popula = mutacao(popula)
            aptidao = fitness(popula)
            individuo_apto, cromossomo_apto = mais_apto(aptidao, popula)
            menor_fitness = menos_apto(aptidao)
            aptos.append(individuo_apto)
            pior_individuo.append(menor_fitness)
            if individuo_apto > melhor_individuo and geracao_atual == 49:
                melhor_individuo = individuo_apto
                melhor_individuo_cromossomo = cromossomo_apto
            media_apt.append(sum(aptidao)/len(aptidao))
            geracao_atual += 1

        if len(aptos) and len(media_apt) == geracoes:
            c.writerow(aptos)
            d.writerow(media_apt)
            r.writerow(pior_individuo)
            var += 1
        geracao_atual = 0


# retono_po = cria_populacao(tamanho_popula, matriz_referencia)
# aptid = fitness(retono_po)
# retono_po = cruzamento(retono_po, [], aptid)
# aptid = fitness(retono_po)
# tempo_fin = time.time()
# print(matriz_referencia)
# print(retono_po)
# print(tempo_fin - tempo_ini)

pop = cria_populacao(tamanho_popula, matriz_referencia)
print(pop[1])
popmutada = mutacao(pop, taxa_mutacao)
print("----------------------")
print(popmutada[1])