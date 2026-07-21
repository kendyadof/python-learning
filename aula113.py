# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acum, produto):
#     print("CUM:",acum)
#     print("produto: ",produto)
#     print()
#     return acum + produto["preco"]

# sugestão de sempre botar um valor inicial, senao o valor inicial vai ser o primeiro produto do iterável, e produto vai ser o segundo do iterável
total = reduce(
    # funcao_do_reduce,
    lambda ac, p: ac + p["preco"], # ac = acumulador, p = produto
    produtos,
    0
)

print("Total é", total)
# ou
# total = 0
# for p in produtos:
#     total += p["preco"]
# print(total)

# ou
# print(sum([p["preco"] for p in produtos]))