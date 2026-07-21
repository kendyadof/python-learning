# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

try:
    import sys
    sys.path.append("C:/Users/Pepe/Downloads")
except ModuleNotFoundError:
    ...

# import aula97_m
from aula97_m import soma, var_mod
# import modulo_piton
# print("este modulo se chama", __name__)
# print("essa pasta é: ", *sys.path, sep="\n")
# print(aula97_m.var_mod)
print(var_mod)
print(soma(2,3))
# print(aula97_m.soma(2,3))