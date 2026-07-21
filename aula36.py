"""
Operadores de atribuição
= += -+ *= /= //= **= %= # todos os operadores aritméticos podem ser usados com operadores de atribuição 
"""
contador = 1

# while contador <= 10:
#     contador = contador + 1 
#     print(contador)


contador += 2
print(contador)
# com string tb funciona

contador ='1'
contador += '2'
print(contador)
# funciona com int e str tb

contador = 10

contador *= '2'

print(contador)

contador = 2
contador **= 10 # 2 elevado a 10
print(contador)

print("Acabou é tetra")