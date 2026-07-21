"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "746824890" # ele fez "74682489070". nove_digitos = cpf[:9]
soma = 0
multi1 = 0
i = 0
j = 10
while i < 9: # for digito in nove_digitos:
    pivot = int(str(cpf)[i]) #  resultado += int(digito) * contador_regressivo; contador_regressivo -=1
    # print(pivot)
    multi1 = pivot * j
    soma = soma + multi1
    i += 1
    j -= 1
# print(soma)
resto = (soma * 10) % 11
digito = 0 if resto > 9 else resto
print(digito)