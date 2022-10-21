import sys
import os

def caminho_arq(caminho, dados, file, deletar):

    os.chdir(caminho)
    lista_arq = []
    apagar = []

    for file in os.listdir():

        if file.endswith(".txt"):
            apagar.append(file)
            lista_arq.append(file)
            file_pacth = f'{caminho}\{file}'
            with open(file_pacth, 'r') as arq:
                leitura = arq.readlines()
        else:
            continue

        lista = []
        nlista = []
        nova = []
        proc = []

        for valor in leitura:
            lista.append(valor)

    dados = lista
    file = lista_arq
    deletar = apagar
    return caminho, dados, file, deletar

def gabarito_regular(caminho, dados, file, deletar):
    lista = dados
    file = file
    proc = []
    apagar = deletar

    for item in lista:
        nova = item[0:19] + ";" + item[19:29] + ";A;" + item[29:]
        proc.append(nova)

    for v in file:
        with open(caminho + "\\" + v + '.txt', 'w') as arquivo:
            for valor in proc:
                arquivo.write(valor.strip() + '\n')

    for d in apagar:
        os.remove(d)


def regular_adaptado(caminho, dados, file, deletar):

    lista = dados
    file = file
    proc = []
    apagar = deletar

    for item in lista:
        nova = item[0:19] + "A;" + item[19:29] + ";A;" + item[29:]
        proc.append(nova)

    for v in file:
        with open(caminho + "\\" + v + '.txt', 'w') as arquivo:
            for valor in proc:
                arquivo.write(valor.strip() + '\n')

    for d in apagar:
        os.remove(d)

def olimpiada(caminho, dados, file, deletar):

    lista = dados
    file = file
    proc = []
    apagar = deletar

    for item in lista:
        nova = item[0:20] + ";" + item[20:30] + ";A;" + item[30:]
        proc.append(nova)

    for v in file:
        with open(caminho + "\\" + v + '.txt', 'w') as arquivo:
            for valor in proc:
                arquivo.write(valor.strip() + '\n')

    for d in apagar:
        os.remove(d)

def olimpiada_adaptada(caminho, dados, file, deletar):

    lista = dados
    file = file
    proc = []
    apagar = deletar

    for item in lista:
        nova = item[0:20] + "A;" + item[20:30] + ";A;" + item[30:]
        proc.append(nova)

    for v in file:
        with open(caminho + "\\" + v + '.txt', 'w') as arquivo:
            for valor in proc:
                arquivo.write(valor.strip() + '\n')

    for d in apagar:
        os.remove(d)

def linguagens(caminho, dados, file, deletar):

    lista = dados
    file = file
    proc = []
    apagar = deletar

    for item in lista:

        asterisco = item[0:30]

        if (asterisco[29] == "*"):
            asterisco = asterisco.replace("*", ";")
            asterisco = asterisco[0:19] + ";" + asterisco[19:29] + ";" + item[30:33] + ";" + "A;" + item[
                                                                                                    33:]
            proc.append(asterisco)
        else:
            asterisco = item[0:19] + ";" + item[19:29] + ";" + item[29:32] + ";" + "A;" + item[32:]
            proc.append(asterisco)

    for v in file:
        with open(caminho + "\\" + v + '.txt', 'w') as arquivo:
            for valor in proc:
                arquivo.write(valor.strip() + '\n')

    for d in apagar:
        os.remove(d)