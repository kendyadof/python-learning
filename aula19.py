"""
>  maior
>= maior ou igual
< menor
<= m enor ou igual
== ingual | um sinal de igual só é atribuição
!= diferente
"""

maior = 2>1
maior_ou_igual = 2>=2
menor = 1<2
menor_ou_igual = 2<=2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

# python -i aula19.py abre o shell python tb,aí será possível usar qualquer variável criada  no momento

# saída:
# (venv) PS C:\Users\Pepe\Documents\pyLearning1> python -i aula19.py
# True
# >>> maior
# True
# >>> maior_ou_igual
# True
# >>> quit()

# para mudar variáveis, deve-se depois SALVAR O ARQUIVO para aplicar as alterações, obviamente.