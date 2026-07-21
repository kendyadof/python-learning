# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path

# fez dps esse caminho do arquivo
CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# texto = """
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa},"""

# template = string.Template(texto)
# print(template.substitute(dados))
# caso tenhja um dadfo faltando no dict, vc pode usar safe_substitute()

class MyTemplate(string.Template):
    delimiter = '$' # poderia ser % tb


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))

# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     texto = arquivo.read()
#     template = string.Template(texto)
#     print(template.substitute(dados))

