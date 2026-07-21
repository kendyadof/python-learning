# escopo da classe e de métodos da classe
class Animal:
    # nome = "Leão"
    def __init__(self, nome):
        self.nome = nome
        # variavel = "valor"
        # print(variavel)
    
    def estapear(self, individuo):
        # print(variavel) # esta fora do escopo
        return f"{self.nome} está estapeando um {individuo}"

    def executar(self, *args, **kwargs):
        return self.estapear(*args, **kwargs)
    
# print(Animal.nome)

leao = Animal(nome="Leão do Proerd")
# print(leao.nome)
print(leao.executar("maconheiro"))