# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
# nao precisa tratar esses dados, tem q retornar multiplicado
# lembrando q multiplicar por ZERO é ZERO
def multi(*args):
    total = 1
    for numero in args:
        total *= numero
        print("Total: ", total, "Número: ", numero)
    return total
        
# nao consegui fazer o usuário inputar tupla, conversão de tipos não funciona (incluí virgula e espaço)
# numeros = tuple(input("Digite uma sequencia de numeros a serem multi (separados por vírgula) :"))
numeros = 1, 2, 3, 4, 5
result = multi(*numeros)
print("Resultado da multiplicação: ", result)
print("Comparação: ", 1*2*3*4*5)



# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
# pode retornar o booleano se quiser. ou um texto de ser par ou ímpar

def ehpar(*args): # luiz otavbio fez sem *args, ele fez numero direto. def par_impar(numero):
    for num in args:
        if num % 2 : # eletinha jogado a condição num % 2 numa variável primeiro
            return False # return f"{numero} é par"
        else: # em tese, este else não é necessário
            return True
    
numero = int(input("Digite um número para verificar se é par: "))
par = ehpar(numero)
print("Is even/par? ", par)
