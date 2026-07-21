# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON = A
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# caminho para luiz otavio era uma constante
# ele tb fez com 3 pessoas e usou o __dict__
import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def write_JSON(dados):
    print()
    if not dados:
        print('Sem dados para usar')
        return
    with open("aula127c.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo,indent=2) 
    print("Dados escritos em JSON.")
    return

# main
# criação de pessoa
p1 = Pessoa("João", 29)
# p2 = Pessoa("Helena", 21)
# p3 = Pessoa("Joana", 11)

# pegar dados
dados = p1.__dict__
# bd = [vars(p1), p2.__dict__,vars(p3)]
# chamada json
# def executa_write(): write_JSON(dados) # explicação no arquivo b
write_JSON(dados)

# print(__name__)
# if __name__ == "__main__":
#     print("ele é o main")

# Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.