from itertools import count
# count é um iterador sem fim (infinito)
# um pouquinho diferente de range.# count vc nao sabe o fim
c1 = count(16, 8)
r1 = range(16,100, 8)

print("c1",hasattr(c1, "__iter__"))
print("c1",hasattr(c1, "__next__"))
# count é um iterável, E é um iterator

print("r1",hasattr(r1, "__iter__"))
print("r1",hasattr(r1, "__next__"))
# print(next(c1))
# print(next(c1))

print("count")

for i in c1:
    if i > 100: # sem isso, é loop infinito
        break
    print(i)

print()
print("range")
for i in r1:
    print(i)