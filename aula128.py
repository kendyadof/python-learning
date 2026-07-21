# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2026  # atributo de classe

    def __init__(self, nome, idade): # self = instância
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls): # cls = class. #assim, nao precisa passar instancia na hora de chamar esse método
        print("hey")

    @classmethod
    def criar_com_50_anos(cls, nome): # cls = class. #assim, nao precisa passar instancia na hora de chamar esse método
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade): # cls = class. #assim, nao precisa passar instancia na hora de chamar esse método
        return cls("Anônima", idade)

p1 = Pessoa("João",34)
p2 = Pessoa.criar_com_50_anos("Helena")
p3 = Pessoa.criar_sem_nome(23)
# Pessoa.metodo_de_classe() # chamando sem precisar da instancia

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)