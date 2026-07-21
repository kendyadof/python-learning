from .modulo import nova_var, var, soma_do_modulo
# from .modulo import *
# poucos casos q o luiz faria import *
# POIS, se no modulo_b por exemplo vc mudaro nome da variavel/função, NAO vai precisar mudar aqui tb, caso vc
# de import *
# MAS, caso precise, vc pode usar Ctrl +F2 pq o vscode conserta pra vc

print("Vc importou ",__name__)


def dobra(x):
    return x*2

# aqui o import * nao seria tão má ideia
