"""
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar: editar o seu código.
"""

# def soma(x,y,z=0):
#     if z:
#         print(f'{x=} {y=} {z=}',x + y + z)
#     else:
#         print(f'{x=} {y=}',x + y)

# soma(1,2)
# soma(3,5)
# soma(100,200)
# soma(7,9,0)

# agora, saber se o z NÃO É none ( q nao é zero, zero é false)
def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}',x + y + z)
    else:
        print(f'{x=} {y=}',x + y)

soma(1,2)
soma(3,5)
soma(100,200)
soma(7,9,0)
soma(y=9, z=0,x=7) # mandando nomeado com outra ordem

# def soma(x,z=None, y):
# ^ tODO PARAMETRO VINDO DPS DE UM Q TA COM VALOR PADRAO PRECISA TER VALOR PADRAO TBM