# try, except, else e finally
# a = 18
# b = 0
string = "Luiz" # str
print("is instance? ",isinstance(string, str))
try:
    a = 18
    b = 0
    # print(b[0]) # outro erro
    # print("Linha 1"[1000])
    c = a / b
    print("Linha 2")
except ZeroDivisionError as ze: # ZeroDivisionError é uma classe
    print("dividiu por zero ", ze.__class__.__name__)

except NameError:
    print("nome nao definido")

except (TypeError, IndexError)  as error: # tupla
    print("type ou index error")
    print("MSG:", error)
    print("Nome:", error.__class__.__name__)

except Exception:
    print("Erro desconhecido.")

print("continue")