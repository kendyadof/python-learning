# recuperar dados da classe a (lendo json)

# ele pegou do arquifvo 127
from aula127a import CAMINHO_ARQUIVO, Pessoa, write_JSON
# executando este arquivo, ele faz o dump do with la do aula127a, porque o importou. Tem q adiar a execução lá nele
import json
class Pessoa: # luiz nao criou pessoa de novo
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def read_JSON(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            if not dados:
                print('Sem dados para usar')
                return
            # p1 = Pessoa(**dados[0])
            # p2 = Pessoa(**dados[1])
            # p3 = Pessoa(**dados[2])

            return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        return
    except json.decoder.JSONDecodeError:
        print("JSON vazio")
        return

# main
# pegar dados
dados = read_JSON("aula127c.json")

if dados:
    # criação de pessoa
    p1 = Pessoa(**dados)
    print("Dados lidos do JSON.")
    print(vars(p1))
else:
    print("nada feito")

# print(__name__)
print()
# Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.