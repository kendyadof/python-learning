# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula99_package # import package nao faz nada

# from aula99_package.modulo import soma_do_modulo # mais preciso

# from aula99_package import modulo
# from aula99_package.modulo import * # nao recomendado

# import aula99_package.modulo
# print(__name__)
# print(*path, sep="\n") # desempacotando

# print(soma_do_modulo(1,2))
# print(aula99_package.modulo.soma_do_modulo(1,2))
# print(modulo.soma_do_modulo(1,2))
# print(var) # quando __all__ explicita la dentro do modulo oq se atribui quando importa com *

# from aula99_package.modulo import soma_do_modulo
# tbm é possivel importar o fala_oi() aqui pois um modulo tb exporta para o outro 

# deste ponto de vista nao tem modulo_b, modulo_b nao é irmão do aula99.py. A importação lá no outro modulo.py, se executado daqui, nao funciona.
# o modulo_b.py portanto nao será encontrado
# FUNCIONARÁ se no modulo.py explicitar no import q o modulo_b deve ser importado do aula99_package



# usando __init__ (arquivo de inicialização):
# quando um módulo é importado, o init é executado
import aula99_package # ao ter o init, o package "vira" um modulo podendo
# oferecer coisas dps de um . , tipo __package__. Luiz chamou isso de
# "enganar" o python

# from aula99_package import soma_do_modulo
print(aula99_package.dobra(2)) # funciona!
print(aula99_package.soma_do_modulo(2,3)) # funciona tbm