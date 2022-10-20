import sys
import os

def caminho_arq(dados):
    os.chdir(dados)
    destino = dados

    for file in os.listdir():
        deletar = file
        if file.endswith(".txt"):
            file_pacth = f'{dados}\{file}'
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

        return lista

def gabarito_regular(dados):
    for item in lista:
        nova = item[0:19] + ";" + item[19:29] + ";A;" + item[29:]
        proc.append(nova)

    with open(destino + "\\" + file + '.txt', 'w') as arquivo:
        for valor in proc:
            arquivo.write(valor.strip() + '\n')
    os.remove(deletar)
    os.system('cls')