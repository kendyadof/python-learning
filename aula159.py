# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields
# dataclass tem init, mas é possivel botar como false. Frozen locka alteração
# de variáveis. FrozenInstanceError
# @dataclass(init=False) # tem repr=False tb. eq=False. 
# @dataclass(frozen = True)
@dataclass(order = True)
class Pessoa:
    # nome: str # = "Missing"
    # sobrenome: str # = "Not sent"
    # idade: int = 100 # introduzida na aula 272. Só pode por valor em IMUTÁVEIS
    # enderecos: list[str] = [] # mutável, e dps de um q foi definido valor padrão 
    nome: str = field(default=" MARIO IS") # = "Missing"
    sobrenome: str = field(default="MISSING")
    idade: int = field(default=100)
    enderecos: list[str]  = field(default_factory=list) # forma certa

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f"{self.nome} {self.sobrenome}"

    # def __post_init__(self):
    #     print("post init")

    # @property
    # def nome_completo(self):
    #     return f"{self.nome} {self.sobrenome}"

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = " ".join(sobrenome)


if __name__ == "__main__":
    # lista = [Pessoa("A", "Z"),Pessoa("B", "Y"),Pessoa("C", "X")]
    p1 = Pessoa("Luiz", "Otávio")
    # p1.nome_completo = "Helena Maria Figueiredo"
    # ordernadas = sorted(lista, reverse=True) # usado com order=True
    # ordernadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome) # usado SEM order=True
    # print(ordernadas)
    # print(p1.nome_completo)
    print(fields(p1))
    print(p1)
    print(asdict(p1))
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1))