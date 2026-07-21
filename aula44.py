"""
For + range
range -> range (start,stop,setp)


for nao depende da funcao range, e viceversa, ok?

"""
# NAO USAR O NOME RANGE PQ JA EXISTE RANGE() NO PYTHON
numeros = range(10) # vai ser só numeros até 10
numeros2 = range(5,10) # start e stop
numeros3 = range(5,10,2) # os tres
numeros4 = range(0, -10, -1)
numeros = range(0, 100, 8)

# print(numeros)

# pra printar tudo ent, é com for

# print(numeros[5])

for i in numeros: # ele fez numero in numeros pra nao ficar confuso
    print(i) # ou seja, printa o contador direto, sem declarar q precisa printas numeros[i]
print("")

for j in numeros2:
    print(j)
print("")

for k in numeros3:
    print(k)
print("")

for l in numeros4:
    print(l)