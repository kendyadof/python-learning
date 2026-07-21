# Generator expression, Iterables e Iterators em python
import sys
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__() # tem __iter__ e __next__
# iterator = iter(iterable)


# print(iterator) # not subscriptable
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# chamar quarta vez dá exceção. O comando for trata isso.

# iterator é um padrão de projeto

# aula de generator expression, iterables e iterators.
# específico de python
# são funções q sabem pausar
lista = [n for n in range(10)] # salva todos na memória
generator = (n for n in range(10)) # está esperando pedir o proximo valor


# generator tb é not subscriptable
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)

