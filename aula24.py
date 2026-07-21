# operadores logicos
# (relembrando)
# strings são iteráveis = pode-se navegar item por item
# in e not in
# 0 1 2 3 4 5 
# O t á v i o
#-6-5-4-3-2-1     tbm tem indices negativos no python (índice -1, a -6, etc)
# ÍNDICE NEGATIVO PRA MIM É MTO BIZARRO
# 
nome = 'Otávio'
print(nome[2]) # = 'á'
print(nome[-4]) # = 'á'

# existem outras coisas iteráveis em python tb, vai-se usar muito isso
print('á' in nome) # True
print('z' in nome) # False
print('vio' in nome) # True
print('zero' in nome) # False
print(10 * '-')
print('vio' not in nome) # False
print('zero' not in nome) # True

nome=input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')