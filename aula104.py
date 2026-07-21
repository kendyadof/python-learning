# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# tb existe o padrao de projeto decorator
# decoradores sao syntax sugar alucar sintatico

def criar_funcao(func): # está é a função decoradora
    def interna(*args, **kwargs):
        #
        print("Vou te decorar")
        for arg in args:
            is_string(arg) 
        resultado = func(*args, **kwargs)
        # 
        print(f"O seu resultado foi {resultado}.")
        print("Ok, agora você foi decorada")
        return resultado
    return interna

# usar arromba em cima faz ele usar a funcao decoradora
# ele vai usar essa funcao marcada no arroba, usando a de baixo como argumento
@criar_funcao
def inverte_string(string):
    print(f"{inverte_string.__name__}")
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")


invertida = inverte_string("Luiz")
print(invertida)