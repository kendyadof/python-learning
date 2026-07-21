# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# da segunda aula:
import sys
sys.setrecursionlimit(1004) # mais q 1000 q é o padrão. Mas de qualquer maneira deve-se tomar cuidado com sua memória
# fim

def recursiva(inicio=0,fim=10):

    print(inicio,fim)

    # caso base (escrito dps, na aula)
    if inicio >= fim:
        return fim



    # caso recursivo= contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())
# proxima aula, sobre recursao ainda

print(recursiva(0,1000)) # o python para em 996

def factorial(n):
    if n <= 1 :
        return 1
    return n * factorial(n-1)

print(factorial(5))
# print(factorial(10))
# print(factorial(100))