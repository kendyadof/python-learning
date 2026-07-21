# Intro às Generator functions em python
# generator = (n for n in range(10000000))
# yield = pausar

def generator(n=0, maximum=10):
    # yield 1 # pausar, entrega 1 como next()
    # print("Continuando...")
    # yield 2
    # print("Mais uma...")
    # yield "jooj"
    # print("terminando")
    # return "ACABOU" # StopIteration: ACABOU
    while True:
        yield n
        n += 1
        if n >= maximum:
            return "termino"
        


# Toda generator function tem um yield

gen = generator(n=5, maximum=8) # é necessário jogar o generator numa variável para efetivamente pausar, ou vai executar a função do zero
# print(gen.__iter__())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen)) # StopIteration: ACABOU

for n in gen:
    print(n)