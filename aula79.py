# exemplo de uso de set
letras = set()
while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if "l" in letras:
        print("FAZUELI")
        break
    print(letras)