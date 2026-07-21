# nome = input('QUAL O SEU NOME????? ') # botar um espaçinho quando terminar a frase, pq o usuário vai digitar algo logo dps, isso no terminal. O OUTPUT do visual code é read-only.
# # INPUT SEMPRE RETORNA STR
# print(f'O seu nome é {nome=}')
# # ao invés de nome={nome}, escreveu {nome=}, isso mostra o nome E o valor da variável
# if nome != 'isshiro nakamura':
#     print("Pelo menos não é isshiro nakamura...")
# else:
#     print("OH SUSHI! VEM AQUI! OH TEMAKI, VEM CÁ!")

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos números é: {numero_1 + numero_2}') # isso resulta em SOMA DE STRINGS, CONCATENAÇÃO

# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

# coerção de variável pra checar algo no meio do caminho:
int_numero_1 =  int(numero_1)
int_numero_2 =  int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}') # isso sim resulta em soma de números

# MAS suponha q eu queria saber oq o usuário digitou antes de converter pra int, se tiver digitado letra, pq letra quebra o programa