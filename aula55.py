"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
artigo wikipedia
artigo docs python.org
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # vira 0.7999999999999999
# isso geralmente nao causa problema, mas se causar temos 3 formas de contornar
# primeira forma de contornar:
print(f'{numero_3:.2f}')
# segunda forma de contornar:
print(round(numero_3, 2)) # passa o numero de casas decimais tb como argumento, mas nao vai aparecer os zeros extras nos prints
# terceira forma de contornar: usar o import la de cima
numero_1 = decimal.Decimal(0.1) 
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3) # mas isso mostra ainda mais casas decimais

# mas aí, faz com str ao invés de float!
numero_1 = decimal.Decimal("0.1") 
numero_2 = decimal.Decimal("0.7")
numero_3 = numero_1 + numero_2
print(numero_3)
#enfim, se preciasr fazer uma conta de super precisão com o dígito lá no fundo,é bom usar esse decimal.Decimal(str)