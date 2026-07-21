"""
Pode "brincar" com este código
"""
for i in range(10): # de 0 a 9
    if i == 2:
        print("i é 2,pulando")
        continue

    if i == 8: # se esse if com break é comentado, aí sim o código chega no final
        print("i é 8, seu else não executará")
        break

    for j in range(1, 3): # 1 e 2
        print(i, j)
else:
    print("for completo com sucesso!")