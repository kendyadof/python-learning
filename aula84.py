import pprint # explicacao linha 44
# list comprehension em python
# list comprehension é uma forma rápida pra criar listas a partir de iteráveis

# print(list(range(10)))
lista = []

# for numero in range(10):
#     lista.append(numero)


# lista = [1 for numero in range(10)] # inclui o numero 1 10 vezes
lista = [numero for numero in range(10)] # colocando à esquerda do for pra falar oq tem q incluir na lista
# print(lista)

# tb é psosivel fazer operações:
lista = [
    numero * 2
      for numero in range(10)]

# print(lista)


# mapeamento de dados em list comprehension:

produtos = [
    {"nome":"p1","preco": 20, },
    {"nome":"p2","preco": 10, },
    {"nome":"p3","preco": 30, },
]

novos_produtos = [
    # produto["preco"]
    # produto["nome"]
    # {"nome": produto["nome"], "preco": produto["preco"]
    # {**produto, "preco": produto["preco"] * 1.05} # aumento de 5% no preço dos produtos
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20 else {**produto} # mapeando somente preço maior do que 20 pra ter aumento de 5%
    for produto in produtos
]
# print(*novos_produtos, sep="\n")

# a lista nova deve ter o mesmo número de elementos da lista anterior, isso é mapeamento de dados

# existe um módulo chamado pprint (print bonito). Não dá pra mandar varios parametros nele
# pprint.pprint(novos_produtos, sort_dicts=False, width=40) # ele tb ordena chaves com sort dicts, largura, etc

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# chamada
# p(novos_produtos)

# suponhetamos (ele nem disse suponhamos)q eu queira do range só até 5:
lista = [n for n in range(10) if n < 5] # é o if do filtro. Inclui só se a condição for verdadeira
# print(lista)


novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20 else {**produto} 
    for produto in produtos
    if (produto["preco"] >= 20 and produto["preco"] * 1.05) > 10 # a multi 1.05 tem q entrar de novo
]
# enfim, com uma lista vc faz outra lista

p(novos_produtos)
