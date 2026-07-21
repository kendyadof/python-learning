# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Iterable, Iterator, Sequence # Luiz fez um por vez

# class MyList(Iterable): 
# class MyList(Iterator): 
class MyList(Sequence): # herdando de Iterable precisa implementar método iter()
    # e herdando de ITerator precisa implementar next()
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
    
    # def append(self, value):
    #     self._data[self._index] = value
    #     self._index += 1
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0 # fazer o ponteiro voltar
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value

    def __len__(self):
        return self._index
    
    def __getitem__(self, index):
        # print("getitem: ",index)
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
if __name__ == "__main__":
    lista = MyList()
    lista.append("Maria", "Helena")
    lista[0] = "João"
    lista.append("Luiz")
    # print(lista._data)
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    # lista[0] = "João"
    # for item in lista: # segundo for usando o iter q nao volta mais, caso
        # nao tenha zerado o next no __next__() antes da stopiteration
    #     print(item)
    print("-----")