#Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.

nome = ['neto', 'monique', 'amanda', 'jonathas', 'arthur', 'thallysson']
idade = [23,22,18,19,19,10]
quantNome = len(nome)
for i in range(quantNome):
    print(f'{nome[i]}  {idade[i]}') 