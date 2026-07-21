# map, partial, GeneratorType e esgotamento de Iterators
# tem tb filter() e reduce()
# filter é um filtro funcional



# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# mesma coisa q o lambda da linha 32:
def filtrar_preco(produto):
    return produto["preco"] > 100

# list comprehension
novos_produtos = [
    p for p in produtos
    if p["preco"] > 10
]

# funcional:
novos_produtos = filter(
    # lambda p: p["preco"] > 10,
    filtrar_preco, # o proprio python executa a func dps, vc nao executa aqui
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)