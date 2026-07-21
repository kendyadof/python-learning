"""
Introdução ao desempacotamento + tipo tuples (tuplas)
"""
# nomes = ["Maria", "Helena", "Luiz"]
# é um pacote de nomes
# quero desempacotar os nomes

# nome1, nome2, nome3 = nomes

# nome1, nome2 = ["Maria", "Helena", "Luiz"] # isso dá erro de "ValueError too many values to unpack (expected 2)"
# nome1, nome2, nome3, nome4 = ["Maria", "Helena", "Luiz"] # isso dá erro de "ValueError not enough values to unpack (expected 4, got 3)"

# como pegar só o primeiro valor e dps o resto?
# nome1, *resto = ["Maria", "Helena", "Luiz"]

# print(nome1, resto)

# convenção: nomear variável como _ , q nao via usar essa variável

_, _, nome, *resto = ["Maria", "Helena", "Luiz"] # isso nao dá erro, o resto fica uma lista vazia
print(nome, resto)