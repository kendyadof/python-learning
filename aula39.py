"""
Iterando strings com while
exercício"""

#  tem índicas na string 
# 0123456789
# -11 ... -1
# iterar a string com um while
nome = "Luiz Otávio" # iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[2])

# fazer:
# nova_string += "*L*u*i*z *O*t*á*v*i*o"
# atribuir iterando as letras da string para uma nova string
nova_string = ""
contador = 0

while contador < len(nome): # ele tb colocou o len(nome) em outra variável, boa prática
    nova_string += nome[contador] # tb colocou nome[contador] em outra variavel
    contador += 1
print(nome)
print(nova_string)