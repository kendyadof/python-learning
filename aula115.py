# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# eu: (o . no inicio de .venv é de ocultar pasta no mac ou no linux)

# para criar um:
# python -V # vai ser a versão do venv
# python -m venv ambiente_venv_extra # ou outro nome para o venv. O primeiro "venv" é um script

# ativar:
# activate
# desativar:
# deactivate.bat (windows)

# ver pasta do python (no powershell):
# gcm python -Syntax
# ao rodar dentro do venv, retorna a pasta do venv

# py -m venv venv2
# venv2\Scripts\activate

# desativar é só:
# deactivate

# # saidas gcm:

# PS C:\Users\Pepe\Documents\pythonreserva> gcm python -Syntax
# C:\cygwin64\bin\python

# (venv2) PS C:\Users\Pepe\Documents\pythonreserva> gcm python.exe -Syntax
# C:\Users\Pepe\Documents\pythonreserva\venv2\Scripts\python.exe


# o venv 1 ja tava configurado no meu
# (venv) PS C:\Users\Pepe\Documents\pyLearning1> deactivate
# PS C:\Users\Pepe\Documents\pyLearning1> gcm python -Syntax                                                                                                                    
# C:\cygwin64\bin\python
# PS C:\Users\Pepe\Documents\pyLearning1> venv\Scripts\activate  
# (venv) PS C:\Users\Pepe\Documents\pyLearning1> 

# ao executar o terminal, o venv costuma ativar instantaneamente