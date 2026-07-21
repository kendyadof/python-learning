""" formatação baasica de strings 
s- string
d - int
f - float
.<numero de digitos>f
x e X - Hexadecimal (ABCDEF0123456789) - x é hexadecimal minusculo e X é hexadecimal maiúsculo
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,1f
Conversion flags - !r !s !a ____r chama o repr. s pega o str, e o a pega o método asci
(isso não é tudo q existe pra formatação de strings)
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.') # suponha q queira preencher de caracteres a variavel até ter 10 caracteres
# 10 caracteres de espaço à esquerda com total de 10 caracteres

print(f'{variavel: <10}.') # direita
print(f'{variavel: ^10}.') # Centro
print(f'{100075489.031543:+,.2f}') #  o sinal de mais pra tb mostrar q o número é positivo
print(f'{1000.75489031543:0>+10,.1f}') # bota 0 na frente do número
print(f'{1000.75489031543:0=+10,.1f}') # força o numero a aparecer antes dos zeros
print(f'o hexadecimal de 1500 é {1500:08X}') 
print(f'{variavel!r}')  # chamando métodos