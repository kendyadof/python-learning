# texto = "Python"

# # índice
# i = 0
# tamanho = len(texto)

# while i < tamanho:
#     print(texto[i], i)

#     i += 1

# # o fim desse laço é previsível, pq é de acordo com o tamanho da string texto.

# senha_salva = "123456"
# senha_digit = ""
# repeticoes = 0

# while senha_salva!=senha_digit:
#     senha= input(f"Sua senha({repeticoes}x): ")
#     repeticoes+=1
# print(repeticoes)
# print("Aquele laço acima pode ter repetições infinitas")

texto = "Python"

novo_texto = ""
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)
    # faz exatamente a mesma coisa q o primeiro letra
    # A variável letra é vc q colocou e dentro do for
print(novo_texto)