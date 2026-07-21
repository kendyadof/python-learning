# operadores logicos
# (relembrando)
# and, or, not
# and todas sao verdadeiras, exceto quando a outra for falsa, aí o and é falso
# Tb existe o None, pra representar um não-valor
# 0    0.0    ''   e False são todos False
# essa primeira aula fala só do and

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = 'senha'
if entrada == 'E' and senha_digitada==senha_permitida:
    print('Entrar')
else:
    print('Sair')

# avaliação de curto circuito:, assim q chegar o false ele nem considera o resto:
# print(True and False and True)

# exemplo: confrontar qualquer valor como booleano:
# print(bool(0.0))
# print(bool(''))
# mas
# print(True and 0 and True) retorna 0