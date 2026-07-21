import aula98_m
# se quiser recarregar  o modulo:
import importlib
# import nao é executado varias vezes pelo for, pois ele é um SINGLETON
print(aula98_m.var)

for i in range(10):
    # print(i)
    # import aula98_m
    importlib.reload(aula98_m) # nao é comum mas pode ocorrer

print("Fim")

# o importlib tb funciona no módulo interativo do python (q começa com >>> no terminal)