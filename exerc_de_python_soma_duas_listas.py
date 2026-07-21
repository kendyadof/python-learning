"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def checa_tam(*args):
    if not args:
        return None
    menor = args[0]
    for arg in args[1:]:
        if len(arg) < len(menor):
            menor = arg
    return menor

def somador(*args):
    lista_aux = []
    i = args[0]
    menor = checa_tam(*args)
    # ou menor = min(len(args[0]),len(args[1]))
    if not menor:
        return None
    if len(args) == 1:
        return args
    tam_menor = len(menor)
    j = args[1]
    k = 0
    soma = 0
    while k < tam_menor:
        soma = i[k]+j[k]
        lista_aux.append(soma)
        k+=1
        soma = 0
    return lista_aux

print(somador(lista_a,lista_b))

# solucao luiz:
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# solucao 2:
# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# solucao 3:
# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)