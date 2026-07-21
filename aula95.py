# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# erros são legais, vc vai lançar erros no seu programa

def nao_aceito_zero(d):
    if d==0:
        raise ZeroDivisionError ("tentando dividir por zero")
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
                f"'{n}' Tipo Errado. "
                f"'{tipo_n.__name__}' enviado."
            )
    return True

def divide(n, d):
# se for dificil nomear a sua função, é porque ela está fazendo muita coisa
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    
    # try:
    return n/d
    # except ZeroDivisionError:
    #     print("algo")
    #     raise # vai relançar a exceção / redundante


print(divide(8,"0"))
# raise ValueError("Deu erro")
# print(456)