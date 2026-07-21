"""
Docstring for aula27
fatiamento de strings
 0123456789
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
 i = inicio
 f = fim
 p = passo
Obs.: a função len retorna a quantidade de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[5]) # = u
print(variavel[-4]) # = u

# fatiamento:
print(variavel[4:]) # = omite o fim e começa pelo m, então vira só mundo
print(variavel[4:8]) # = se quiser pegar o final, então é índice 8 = mund
# se omitir o final, ele sabe q tem q ir até o final

print(variavel[0:5]) # Olá m
print(variavel[:5]) # Olá m = tb omite o final
print(variavel[-8:-2]) # lá mun = lembre-se de q o caractere espaço tb é contado. Nesse caso, índice 3

print(len(variavel[3])) # = 1
print(len(variavel)) # = 9
# len retorn obj do tipo Sized, int, mais pra frente ele vai explicar.
# tbm ensinará a criar objetos
print(variavel[0:len(variavel):1]) # fatiamento literal da string
# o passo p é em quantos caracteres ele vai contar, o padrão é 1 (lendo 1 por 1)

print(variavel[0:9:2]) # = Oámno = foi de 2 em dois, mas do começo ao fim
print(variavel[0:9:4]) # = Omo = foi de 4 em 4
print(variavel[::-1]) #  assim ele conta, mas vai por trás, ou seja, ele inverte a string
print(variavel[0:9:-1]) # isso fica vazio, porque o indice tem q ser vazio tb, então o correto é o da prox linha
print(variavel[-1:-10:-1]) # agora sim, ou melhor, mis aroga