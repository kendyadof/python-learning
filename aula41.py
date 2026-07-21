"""
while else
Não é um recurso q o luiz otavio nao gosta q é especifico de python
mas vai ensinar q existe
"""
string = "Valor qualquer"

i = 0
letra = ""
while i < len(string):
    letra = string[i]

    if letra == " ":
        break

    print(letra)
    i += 1
    
else:
    print("O else foi executado / nao encontrei um espaço na string (caso a string nao tivesse um espaço)")
    # quando o laço while termina, o else é executado
    # é quase, mas nao é a mesma coisa q só fazer um comando fora do while
    # exemplo, se der break, o else NAO é executado.

print("Fora do while. ")