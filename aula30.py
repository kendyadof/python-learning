"""
CONSTANTE = "variáveis que não vão mudar"
no python não *existe*, mas tem uma convenção de usar letras maiúsculas pra coisas q nao vao mudar no código

Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # lcal em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

# associar expressão a uma variavel vc consegue dar um nome a esse trecho de codigo e deixar teu código mais LEGÍVEL
if vel_carro_pass_radar_1:
    print("Passou da velocidade do radar 1")

    # if local_carro in [LOCAL_1 - RADAR_RANGE, LOCAL_1, LOCAL_1+RADAR_RANGE]: # o q eu fiz não pega um range todo, apesar de pegar esse
    # ele tb fez um if fora do outro, independetes, eu fiz dentro
if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print("Foi  multado em radar 1")
    
else:
    ...

# dica dele mesmo: deixar o código legível assimm, com variáveis