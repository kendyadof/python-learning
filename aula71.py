"""
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
# Lembre-te de desempacotamento
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x,y):
#     return x + y
# passando argumentos nao nomeados:

def soma(*args): # passar uma quantidade ilimitada de argumentos não-nomeados
    # args = list(args)
    # print(args, type(args))
    total = 0  # acumulador
    for numero in args:
        total += numero
        # print("Total ", total, ". número atual: ", numero) 
        return total
soma_n = soma(1, 2, 3)
print("Soma = ",soma_n)

soma_n = soma(4, 5, 6)
print("Soma = ",soma_n)

soma_n = soma(1,2,3,4,5,6,7, 78, 10)
print("Soma = ",soma_n)

# agora oq tem no python:
print(sum((1,2,3,4,5,6,7, 78, 10)))

# se fizer isto, vai mandar uma tupla dentro de outra tupla na funcao soma:
# numeros = 1,2,3,4,5,6,7, 78, 10
# outra_soma = soma(numeros)

# oq pode sef azer ent , é DESEMPACOTAR a sequencia
numeros = 1,2,3,4,5,6,7, 78, 10
outra_soma = soma(*numeros)

# *args EMPACOTA oq enviar pra função dentro de uma tupla
# soma(*numeros) DESEMPACOTA uma tupla, para enviar como parâmetro para a função