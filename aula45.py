"""
como o for funciona por baixo dos panos?
iteravel ->  str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entregue  o próximo valor
iter -> me entregue seu iterador


iteravel tem um metodo chamado iter
metodo é uma ação dentro de um objeto
texto = "Luiz"
texto.zfill()

a primeira coisa q o for faz é chamar o iterador do objeto
"""

# numeros = range(0,100,8)

# for numero in numeros:
#     print(numero)

texto = "Luiz".__iter__()
print(texto) # saída <str_ascii_iterator object at 0x0000017B16881150>

# o python tem uma outra maneira de pedir o iter:
texto = iter("Luiz")
print(texto)
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__()) # dá erro quando chama next e nao tem outro valor
# print(next(texto)) # mesma coisa q o .__next__()
# enfim
texto = "Luiz"
iterador = iter(texto)

# for letra in texto
# for ve quem é o texto, e aí ele chama o iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
# enfim, é isso q o for faz

# for letra in texto: print(letra)