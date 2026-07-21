# __all__ = [ # interfere no import *
#         "var",
#         "soma_do_modulo",
#     ]

# from modulo_b import fala_oi
# portanto, melhor explicitar q o modulo_b vem do aula99_package, no caso de
# ser executado o aula99.py como main, pois o aula99 nao enxergaria o modulo_b sem isso ao executar o modulo.py, pois 
# este tb está importanto o modulo_b.py
# CASO execute este aqui, NÃO explicite aula99_package, pois ele ja conhece essa pasta e tentará importar outra
var = "alguma coisa"

# em import, . tb significa a propria pasta
# from .modulo_b import fala_oi


def soma_do_modulo(x, y):
    return x + y

nova_var = "jooj" # está nao está no __all__

# fala_oi()