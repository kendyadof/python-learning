"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1

    lista de listas
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
# meu algoritmo (no final ficou errado pq nao retorna o primeiro duplicado encontrado):
pivot = 0
lista_de_repetidos = []
repetidos = set()
tem_repetido = False
atual = 0
element=0
primeiro = False
lista_de_returns = set()
lista_de_lista_de_returns = []
for lista in lista_de_listas_de_inteiros:
    size = len(lista)
    end = len(lista)-1
    while element < size:
        while pivot < size:
            if pivot != element:
                if lista[element] == lista[pivot]:
                    tem_repetido = True
                    primeiro = True
                    repetidos.add(lista[element])
                if primeiro:
                    lista_de_returns.add(lista[element])
            pivot += 1
        pivot = 0
        element+=1
    # pivot = 0
    element = 0
    if not tem_repetido:
        repetidos.add(-1)        
    lista_de_repetidos.append(repetidos)
    # for e in repetidos:
    #     lista_de_returns.add(e)
    #     break
    lista_de_lista_de_returns.append(lista_de_returns)
    repetidos = set()
    lista_de_returns = set()
    tem_repetido = False
    primeiro = False
# set_de_lista_de_repetidos = set(lista_de_repetidos)
print("Lista inteira: ",lista_de_repetidos)
print()
print("Lista final: ", lista_de_lista_de_returns)


# CHAT GPT / DUCK AI (certo) (mais ou menos oq o luiz otavio fez tb):
# def primeiro_duplo(lista):
#     visto = set()
#     for i in lista:
#         if i in visto:
#             return {i}
#         visto.add(i)
#     return {-1}

# lista_de_sets = [
#     primeiro_duplo(lista) for lista in lista_de_listas_de_inteiros
# ]
# print(lista_de_sets)

# luiz otavio:

# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista)
#     )        
        

