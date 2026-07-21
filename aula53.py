"""
enumerate - enumera iteráveis (índices)
ao inves de imprimir os indices com a lista em um loop
"""
lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

lista_enumerada = enumerate(lista)
print(lista_enumerada)
# o objeto printado é um iterator
print(next(lista_enumerada)) # (0, 'Maria')
# chamando unm next direto nele.

for item in lista_enumerada:
    print(item)

# se der for mais uma vez no mesmo iterator, nao vai printar duas vezes, pq nao tem mais proximo valor no iterator
# eu já "consumi" esses valores
print("O que tem na lista enumerada: ",lista_enumerada)

for item in lista_enumerada:
    print(item)

# enfim, geralmente, quando se usa enumerate(), não se atribui a uma variável assim.
# fazendo assim, aí dá pra fazer quantos for vc quiser nele:
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)

# Agora, vamos printar como uma lista pq a gente quer ver os valores:

lista_enumerada = list(enumerate(lista))

print(lista_enumerada) # saída: [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# enfim, no python, nao tem como dar print só num indice assim, diferente de outras linguagens, tipo php e javascript
# o enumerate entao vai criar um outro iterável dentro da lista -> ele cria uma tupla com indice,valor indice,valor ...

# é possível tb fazer:
# lista_enumerada = list(enumerate(lista, start=10)) # vai começar do 10, nao do 0, mas nao de décimo índice, ele vai botar 10,Maria e etc...

# tb acontece o mesmo aqui, se fizer:
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
# ou
for indice, nome in enumerate(lista): # (isso é um desempacotamento)
    print(indice, nome)

# e ainda é possível:
for tupla_enumerada in enumerate(lista): # (isso é um desempacotamento)
    print("FOR da tupla: ")
    for valor in tupla_enumerada:
        print(f'\t{valor}') # \t é um tab na string