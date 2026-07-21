"""
listas em python
tipo list - mutável
suporta varios valores de qualkquer tipo
conhecimentos reutilizáveis - índices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321  
string = "ABCDE"
# é possivel ACESSAR um indice da string,e nao pode mudar o valor desse indice

# lista = []
# print(bool(lista)) # = False, lista vazia
# print(bool([])) # = False, lista vazia
# print(lista, type(lista))
#         0    1         2          3     4
#        -5    -4       -3         -2     -1
lista = [123, True, "Luiz Otávio", 1.2, [] ]
print(lista[2].upper(), type(lista[2]))

lista[-3] = "Maria"
print(lista)
print(lista[2], type(lista[2]))

# parte 2 da aula
# append, insert, pop, del, clear, extend, +
# CRUD - create, read, update, delete

lista = [1, 2, 3, 4] # create
lista[2] = 300 # update

# pra deletar:
del lista[2] # Delete 

print(lista) # dps de del, o python reorganiza a lista, com 1 índice a menos
print(lista[2]) # read 

# dica: fazer um del no começo de uma lista de 10000 elementos vai fazer 9998 irem pra esquerda e isso requer MUITO processamento. Evitar mover uma lista muito grande.
#   É mais interessante mexer com o fim dela

lista.append(50) # adicionar coisas na lista, no final dela
print(lista)
lista.pop() # Remove o ultimo elemento da lista
lista.append(60)
lista.append(70)
# pode-se atribuir o removido a uma variável:
ultimo_valor = lista.pop()
print(lista, "Removido: ", ultimo_valor)
# pop retorna o tipo de valor inicial da lista, nesse caso retorna int
# tb pode-se dar pop num índice específico)
ultimo_valor = lista.pop(3)

print(lista, "Removido: ", ultimo_valor)



# parte 3 :

# append - adiciona um item ao final
# insert - adiciona um item no índice escolhido
# pop - remove do final ou do índice escolhido
# del - apaga um índice
# clear - limpa a lista
# extend - estende a lista
# + - concatena listas

lista = [10, 20, 30, 40]
lista.append("Luiz")
nome = lista.pop()
# del lista[-1] # deletar o ultimo item da lista | -1 vai ser sempre o último item da lista
# lista.clear() # limpar a lista
lista.insert(0, 5) # insert recebe 2 args: índice e valor # todos os itens da lista são movidos pra frente nesse caso
print(lista, nome)
# é comum errarem e tentarem acessar um indice q nao existe: retorna IndexError list index out of range

lista.insert(100, 5) # mesmo nao existindo o indice, ele joga pro final da lista, mas na opinião do luiz deveria dar error isso
# só vai dar erro no print por exemplo




# parte 4

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # concatenação, + tem o polimorfismo
print("lista C: ", lista_c)

lista_d = lista_a.extend(lista_b)
print("Lista D: ", lista_d) # = None
# o extend é uma ação q não retorna nada, no caso, ele trabalha coma  lista_a. A lista A q ficou alterada

print("Lista A extendida: ", lista_a)
# ou seja, não é possível pegar a função q nao retorna nada e colocar numa variável




"""
Cuidado com dados mutaveis (ELE COLOCOU NO MESMO ARQUIVO AULA48.PY)
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = "Luiz"
# nome[1] = "D" # não é possível
noutra_variavel = nome
nome = "João" # garbage collector  do python toma conta das memórias q nao estao sendo mais utilizadas
# só alterou o valor, de botar uma variavel str pra outra variavel str
print(nome)
print(noutra_variavel)

lista_a = ["Luiz", "Maria"]
lista_b = lista_a # nesse caso de listas, o valor de lista_a nao vai pra lista_b, ele vai fazer os dois apelidos/variáveis apontarem para a mesma memória


lista_a[0] = "Qualquer coisa" # Fazendo isso vai alterar a lista b
print(lista_b)
# enfim, tem q tomar cuidado com tipos imutáveis assim
# isso não ocorre com imutável

# pra copiar mesmo o valor assim, é com um método COPY()
# 
lista_b = lista_a.copy()
lista_a[0] = "Qualquer coisa 2 "

print("lista a: ", lista_a)
print("lista b: ", lista_b)