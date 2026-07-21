# if / elif    / else
# entrada = input('Voce voce voce voce voce quer?')

# print('Você quer')
# print('Você não quer')

# if é usado pra quebrar o programa em blocos de código

entrada = input('Voce voce voce voce voce quer? ') # na aula era "vc quer entrar ou sair?"

if entrada == 'sim': # condição booleana
    print('Você quer')
    # o tab determina estar dentro do if
elif entrada == 'nao' : # elif depende do if
    print('Você não quer')
else: # else tb depende do if, e é sempre a última opção
    print('fala direito caraio')