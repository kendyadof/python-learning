# dir, hasattr e getattr em Python
string = "Luiz"
metodo = "upper"

# dá um dir no objeto pra achar uma função
# print(string)

if hasattr(string, metodo):
    print("Existe upper")
    print(getattr(string, metodo)()) # checar se o método existe E executando ele
    # print(string)
else:
    print("Não existe o método", metodo)

