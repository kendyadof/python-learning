import pprint
import copy
# copy, sorted, produtos.sort
# from dados import produtos

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
def p(v):
    pprint.pprint(v, width=40)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# fazer list comprehension,. à esquerda de for

# novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, "preco": round(produto["preco"] * 1.10, 2)}
    for produto in produtos
]

# luiz otavio:
# novos_produtos = [
#     {**p, "preco": round(p["preco"] * 1.1, 2)} # desempacotando
#     p for p in copy.deepcopy(produtos)
# ]
# dps ele tirou esse deepcopy pq nao precisava, mas ficar ligado pra nao alterar a lista original


p(novos_produtos)
# print(id(novos_produtos))
# print(id(produtos))
# print(produtos.__class__.__name__)
# for produto in produtos:
#     print(produto.__class__.__name__)
#     novos_produtos.append()


# enfim, lista de dicts.





# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda x: x["nome"], reverse=True)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print("")
print("ordenados por nome decrescente: ")
p(produtos_ordenados_por_nome)

print("")
print("ordenados por preço crescente: ")
# produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda x: x["preco"], reverse=False)
p(produtos_ordenados_por_preco)