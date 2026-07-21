""" intepolação básica de strings
s- string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) - x é hexadecimal minusculo e X é hexadecimal maiúsculo
"""

nome = 'Luiz'
preco = 1000.95897643
# variavel = 'Luiz, o preço total foi R$1000.95' - como fazer com interpolação?
variavel = '%s, o preço total foi R$%.2f' % (nome, preco) # vai passar as variáveis depois da string com o %, e as variaveis
# %.2f é oq faz duas casas decimais do float. Interpolação vem lá do C mesmo
print(variavel)
print("O hexadecimal de %d é %x" % (15,15))
print("O hexadecimal de %d é %04x" % (15,15)) # ele faz com 4 dígitos, mesmo sendo 000f
print("O hexadecimal de %d é %08X" % (2147483647,2147483647)) # ele faz com 4 dígitos, mesmo sendo 000f

# enfim, dá pra interpolar pra fazer mudança de tipos e conversões no print
# se nao quiser fazer formatação assim, tem outras formas: f strings, format(), e interpolação. Otavio prefere f strings