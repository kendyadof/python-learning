import json
pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55}
    ],
    "altura": "1.7",
    "numeros_preferidos": (2,4,6,8,10),
    "dev": True,
    "nada": None,
}
# json é bom pra salvar dicionários de python
# "set": {1, 2, 3}
# "set is not JSON serializable"


with open("aula117.json", "w", encoding="utf-8") as arquivo:
    # fazer dump() diferente de dumpas()
    json.dump(pessoa, arquivo,indent=2) # ensure_ascii=false, caso nao queira q acentos virem u0100 etc

    # json nao pega funções, classes, ou sets. Mas coisas convertidas sim.
    # uma tupla vira uma lista no json, ent ao converter de volta será uma lista

# para ler json e escrever em variável:
with open("aula117.json", "r", encoding="utf-8") as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa)) # vira um dict
    print(pessoa["nome"])