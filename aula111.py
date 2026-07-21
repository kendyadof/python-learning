# map, partial, GeneratorType e esgotamento de Iterators
# tem tb filter() e reduce()
from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem,2)


aumentar_dez_porcento = partial(aumentar_porcentagem,porcentagem = 1.1)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 
     "preco": aumentar_dez_porcento(p["preco"])}
    for p in produtos
]

def muda_preco_de_produtos(produto):
    return {
        **produto,
          "preco": aumentar_dez_porcento(
              produto["preco"]
          )
    }

novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

# generator
novos_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, "__iter__"))
print(hasattr(novos_produtos, "__next__"))
# checar se é generator
print(isinstance(novos_produtos, GeneratorType))

# print(list(novos_produtos)) # o iter ja foi esgotado, nao da pra usar de novo, teria q fazer:


# novos_produtos = list(map(
#     muda_preco_de_produtos,
#     produtos
# ))
# assim teria como iterar livremente sobre o map, q foi convertido em uma lista


# fazendo com lambda
print(
    list(map(
        lambda x: x * 3,
        [1,2,3,4]
    )
))
