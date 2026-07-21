# conversão de tipos, coerção
# type convertion, typecasting, coercion é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
# print(1+1)
# print('a' + 'b') # polimorfismo, concatenou (só aparece em linguagens dinâmicas)

print(int('1'), type(int('1'))) # '1' + 1 dá erro, em javascript e php não, pq seria tipagem fraca, o python é forte
print(type(float('1') + 1)) # resultará em float, pois é um float com int
# o primeiro a ser executado é o parênteses de dentro, depois vai indo pra fora

print(bool('')) # = False
print(bool(' ')) # = True

print(str(11) + 'b')