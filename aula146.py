# ele pulou a 145
# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError("a", "b", "c") # _ pra caso seja palavra reservada, mas nesse caso nao é
    exception_.add_note("olha olha olha")
    exception_.add_note("errou faustão")
    raise exception_

try:
    # 1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)              
    print()
    exception_ = OutroError("vou te comer")
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note("Mais uma")
    
    raise exception_ from error