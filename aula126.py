# __dict__ e vars para atributos de instância

class Pessoa:
    # atributo = "valor"
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa("João", 35)
# p1.nome = "EITA"
# del p1.nome
# print(p1.idade)
# p1.__dict__["outra"] = "coisa"
# p1.__dict__["nome"] = "EITA"
# del p1.__dict__["nome"]
# print(p1.__dict__)


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

print(vars(p1))
# dica do luiz otavio: dicionario jogar num json
print(p1.nome)