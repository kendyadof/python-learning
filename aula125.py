# Atributos de classe
# ANO_ATUAL = 2025

class Pessoa:
    # atributo = "valor"
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100

    def get_ano_nasc(self):
        # return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa("João", 35)
p2 = Pessoa("Helena", 12)
print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1 # isso altera para todas as instâncias
print(p1.get_ano_nasc())
print(p2.get_ano_nasc())