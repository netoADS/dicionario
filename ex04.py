# Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.
listaUni = {}
nome = []
idade = []


def insertNome():
    return input('Insira um nome: ')


def insertIdade():
    return int(input('Insira uma idade: '))


while True:
    nome = insertNome()
    if nome == '':
        break

    idade = insertIdade()
    listaUni[nome] = idade
c = 0

for l, d in listaUni.items():
    nome.extend([l])
    c += 1

print(nome, idade)