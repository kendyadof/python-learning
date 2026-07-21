"""
Repetições
aula de while 2
"""

while False: # condição jamais será sanada
    print("EITA") # código unreachable

contador = 0

while contador < 10: # enquanto contador for menor q 10, execute este código
    contador = contador + 1 # dentro do while, manipular o contador
    print(contador)

print("Acabou é tetra")