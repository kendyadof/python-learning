"""
Flag ( Bandeira) - marcar um lovcal
None = não valor
is e is not = é ou não é (tipo,valor ,identidade)
id = identidade
"""
v1 = "a" # apelido pra algo q está na memória
v2 = "a" # python verá q são dois valores iguais e podem ser o mesmpo valor na memória pra ser o mesmo endereço de memória
# vcpode ver a identidade da variável com a funçlão id()
print(id(v1))
print(id(v2))
# mas se mudar a v2 = b, aí o endereço muda, claro

condicao = True # colocar uma flag aqui, aí o debugger vai indo, pra entender a atribuição de none e is none na variável
passou_no_if = None
# parte da aula de flags:
if condicao: 
  # exemplo, é ruim colocar uma variável dentro do if, sem ter declarado ela fora
  passou_no_if = True
  print("Faça algo")
else:
  # passou_no_if = None
  print("Não faça algo")
# print(passou_no_if, passou_no_if is None) # ao invés de usar == None
# print(passou_no_if, passou_no_if is not None) 

if passou_no_if is None:
  print("Não passou no if")

if passou_no_if is not None:
  print("Passou no if")

