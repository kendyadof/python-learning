"""
Tipo tupla - Uma lista imutável
"""

nomes = ["Maria", "Helena", "Luiz"] # criando lista
# pra ser tupla (tuple) é só tirar os colchetes:
# nomes = "Maria", "Helena", "Luiz"
# nomes[1] = "outro" # tuple does not support item assignment
# _, _, nome, *resto = nomes
print(nomes)

# a tupla é um pouco mais eficiente q a lista, a lista é mais lenta

# sempre q eu trabalhar com uma lista mas sem editar ela, eu posso usar uma tupla
print(nomes[-1])

# tb da pra criar assim:
# nomes = tuple(nomes)
# nomes = list(nomes)