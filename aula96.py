# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
sys.exit()

platform = 'A MINHA' # Kkkkkkkkk
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform
# nomes nao devem ter mesmo nome q objeto de modulo
print(platform) # win32

# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex # poderia separar por virgula tb
from sys import platform as pf

print(pf) # prato feito

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import *
# os nomes das variáveis vão estar disponíveis. Importando todos os nomes
print(platform)
exit()