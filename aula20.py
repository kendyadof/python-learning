primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
# utilizando as variáveis e parametros. Usar if elif else e algum operador de comparação
# ELE TB QUERIA Q B FOSSE MAIOR Q A, O PROPRIO PYTHON FAZ ISSO, NAO É PRA CONVERTER PRA FLOAT OU INT
# int_primeiro_valor = float(primeiro_valor)
# int_segundo_valor = float(segundo_valor)

if primeiro_valor > segundo_valor:
    formato = 'primeiro_valor={0} é maior do que segundo_valor={1}'.format(primeiro_valor, segundo_valor)
    print(formato)
elif primeiro_valor < segundo_valor:
    formato = 'segundo_valor={0} é maior do que primeiro_valor={1}'.format(segundo_valor, primeiro_valor)
    print(formato)
else:
    formato = 'primeiro_valor={0} é igual a segundo_valor={1}'.format(primeiro_valor, segundo_valor)
    print(formato)

# não consegui escrever "segundo_valor='2' ", escrevi segundo_valor=2 sem as aspas simples, entende?"

# ele tinha feito sem elif e nao tem esse  de um ser igual ao outro mas enfim. É q o <= dele tava no else e ia deixar o segundo sendo maior pq fodase.
# dps ele percebeu, ele botou if tal então valor é MAIOR OU IGUAL ao segundo valor
# ele tb fez por f strings = f'{primeiro_valor=} é maior ' f'do que {segundo_valor=}'