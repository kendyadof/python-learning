# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

def checa_tam(*args):
    if not args:
        return None
    menor = args[0]
    for arg in args[1:]:
        if len(arg) < len(menor):
            menor = arg
    return menor

def zipper(*args):
    lista_aux = []
    i = args[0]
    tupla_aux = []
    menor = checa_tam(*args)
    if not menor:
        return None
    if len(args) == 1:
        return args
    tam_menor = len(menor)
    j = args[1]
    k = 0
    while k < tam_menor:
        tupla_aux.append(i[k])
        tupla_aux.append(j[k])
        lista_aux.append(tuple(tupla_aux))
        k+=1
        tupla_aux = []
    return lista_aux

print(zipper(lista1,lista2))

# solucao do luiz:
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))