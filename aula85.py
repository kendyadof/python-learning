# possível fazer for dentro de for com list comprehension (indo poela esquerda do for)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y)) # nao tem como enfiar dois valores num índice da lista, tem q ter um tipo de dado q aceita mais de um valor

lista = [
    (x,y) # oq está antes do for, ao lado esquerdo, é oq vai ser incluído na lista. É oq vai ser usado para o mapeamento
    for x in range(3)
    for y in range(3)
] # está sendo a mesma coisa


# agora com lisrt comprehension junto
lista = [
    # [x for y in range(3)] # nova list comprehension
    [(x,letra) for letra in "Luiz"]
    for x in range(3)
    
]

print(lista)