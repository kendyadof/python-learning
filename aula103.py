# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# tb existe o padrao de projeto decorator

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

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")

inverte_checando = criar_funcao(inverte_string)
invertida = inverte_checando("Luiz")
print(invertida)