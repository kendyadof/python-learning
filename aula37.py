"""
aula de while 3
continue
"""


contador = 0

while contador < 100: # 
    contador += 1 #  tomar cuidado para o contador não ficar sem incremento dentro do while, deixando o while loopado
    
    # ele sempre sai com break
    # com continue, ele pula
    if contador == 6:
        print("Não vou mostrar o 6")
        continue # pula pro próximo laço do while, final, ele não printa o 6
    
    if contador >= 10 and contador <= 27:
        print("Não vou mostrar o", contador)
        continue # pula pro próximo laço do while, final, ele não printa do 10 ao 27

    print(contador)
    if contador == 40:
        break # ele sempre sai com break
        # com continue, ele pula


print("Acabou é tetra")

