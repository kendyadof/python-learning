"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC) abstrata
    sacar()
    ContaCorrente class
    ContaPoupanca class

Pessoa (ABC) abstrata
    Cliente ( PEssoa)
        Clente -> Conta

Banco (tem autenticação)
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
NAO USEI TIPAGEM Q ELE ENSINOU DPS PQ QUEBRA TUDO DO MEU CÓDIGO E
ELE TB NAO USOU SETTER E GETTER ENT WHATEVER
"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = None
        self.agencia = agencia
        self._numero_conta = None
        self.numero_conta = numero_conta
        self._saldo = 0
        self.saldo = saldo

    @property
    def agencia(self): 
        return self._agencia
    
    @agencia.setter
    @abstractmethod
    def agencia(self, agencia):  
        return self._agencia
    
    @property 
    def numero_conta(self): 
        return self._numero_conta
    
    @numero_conta.setter 
    @abstractmethod
    def numero_conta(self, numero_conta):  
        return self._numero_conta
    
    @property 
    def saldo(self): 
        return self._saldo
    
    @saldo.setter 
    @abstractmethod
    def saldo(self, numero_conta):  
        return self._saldo
    
    @abstractmethod
    def depositar(self, saldo, valor): # depoisto é abstrato assim como sacar??
        ...
    
    @abstractmethod
    def sacar(self, saldo, valor):
        ...
    
    @abstractmethod
    def consulta_saldo(self):
        ...
    
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = None
        self.nome = nome
        self._idade = 0 
        self.idade = idade

    @property 
    def nome(self): 
        return self._nome
    
    @nome.setter 
    @abstractmethod
    def nome(self, nome):  
        ...
    
    @property 
    def idade(self): 
        return self._idade
    
    @idade.setter 
    @abstractmethod
    def idade(self, nome):  
        ...

class ContaCorrente(Conta):
    limite_extra = 1000
    def __init__(self, *args, **kwargs): # sobrepondo init e atributos
        # print("EI burlei o sistema")
        super().__init__(*args, **kwargs)

    @Conta.agencia.setter
    def agencia(self, agencia):  
        self._agencia = agencia

    @Conta.numero_conta.setter
    def numero_conta(self, numero_conta):  
        self._numero_conta = numero_conta

    @Conta.saldo.setter
    def saldo(self, saldo):  
        self._saldo = saldo

    def depositar(self, valor): # depoisto é abstrato assim como sacar??
        self.saldo += valor
        print(f"Depositado:{valor}, Saldo:{self.saldo}, Limite: {self.limite_extra}")
    
    def sacar(self, valor):
        try:
            if (self.saldo - valor) < 0:
                if (self.limite_extra - valor) < 0:
                    raise ValueError("Saldo e Limite insuficientes!")
                self.limite_extra -= (valor - self.saldo)
                self.saldo += (valor - self.saldo)
            self.saldo -= valor
            print(f"Sacado:{valor}, Saldo:{self.saldo}, Limite: {self.limite_extra}")
        except ValueError as exception:
            print("Erro: ", exception)

    def consulta_saldo(self):
        return self.saldo
    
    def consulta_limite(self):
        return self.limite_extra

class ContaPoupanca(Conta):
    def __init__(self, *args, **kwargs): # sobrepondo init e atributos
        # print("EI burlei o sistema")
        super().__init__(*args, **kwargs)

    @Conta.agencia.setter
    def agencia(self, agencia):  
        self._agencia = agencia

    @Conta.numero_conta.setter
    def numero_conta(self, numero_conta):  
        self._numero_conta = numero_conta

    @Conta.saldo.setter
    def saldo(self, saldo):  
        self._saldo = saldo

    def depositar(self, valor): # depoisto é abstrato assim como sacar??
        self.saldo += valor
        print(f"Depositado:{valor}, Saldo:{self.saldo}. Conta poupança não possui limite")
    
    def sacar(self, valor):
        try:
            if (self.saldo - valor) < 0:
                raise ValueError("Saldo insuficiente!")
            self.saldo -= valor
            print(f"Sacado:{valor}, Saldo:{self.saldo}. Conta poupança não possui limite")
        except ValueError as exception:
            print("Erro: ", exception)

    def consulta_saldo(self):
        return self.saldo

class Cliente(Pessoa):
    # conta = None # ContaCorrente() | ContaPoupanca()
    def __init__(self, conta, nome, idade): # sobrepondo init e atributos
        # print("EI burlei o sistema")
        super().__init__(nome, idade)
        self._conta = None
        self.conta = conta
    
    @Pessoa.nome.setter
    def nome(self, nome):  
        self._nome = nome

    @Pessoa.idade.setter
    def idade(self, idade):  
        self._idade = idade


    @property 
    def conta(self): 
        return self._conta
    
    @conta.setter 
    def conta(self, conta):  
        self._conta = conta
        return self._conta


class Banco:
    def __init__(self, clientes, agencias, contas):
        self.clientes = clientes
        self.contas = contas
        self.agencias = agencias

    def autentica(self, nome, agencia, conta ) -> Cliente : 
        try:
            tem_cliente = False
            # agencia_autenticada = False
            # conta_autenticada = False
            cliente_autenticado = None
            for cliente in self.clientes:
                if nome == cliente.nome and agencia == cliente.conta.agencia \
                and conta == cliente.conta.numero_conta:
                    tem_cliente = True
                    # agencia_autenticada = True
                    # conta_autenticada = True
                    cliente_autenticado = cliente
                    break
        
            if not (tem_cliente):
                raise ValueError(f"Cliente/conta/agencia não encontrado!")
                    # Nome: {nome}, Agência:{agencia}, Conta: {conta}")      
        except ValueError as exception:
            print("Erro: ", exception)
            cliente_autenticado = None
        return cliente_autenticado
    
# Main:
co = ContaCorrente(1,4,0)
co2 = ContaPoupanca(2,5,0)

c1 = Cliente(co, nome="João", idade=30)
c2 = Cliente(co2, nome="Maria", idade=20)

b = Banco([c1,c2],[c1.conta.agencia, c2.conta.agencia], [c1.conta.numero_conta, c2.conta.numero_conta])

nome1 = input("Bem-vindo ao banco! Qual seu nome? ")
agencia1 = input("Digite o número da agência: ")
conta1 = input("Digite o número da conta: ")
if agencia1.isdigit():
    agencia1 = int(agencia1)
if conta1.isdigit():
    conta1 = int(conta1)

cliente_autenticado = None

cliente_autenticado = b.autentica(nome1, agencia1, conta1)
if cliente_autenticado:
    print("Autenticado com sucesso!")
    while True:
        operacao = input("Digite operacao (sacar, depositar, saldo, sair): ")

        if operacao == "sacar":
            valor = int(input("Digite o valor: "))
            cliente_autenticado.conta.sacar(valor)
            continue
        elif operacao == "depositar":
            valor = int(input("Digite o valor: "))
            cliente_autenticado.conta.depositar(valor)
            continue
        elif operacao == "saldo":
            saldo1 = cliente_autenticado.conta.consulta_saldo()
            print("Saldo:",saldo1)
            if isinstance(cliente_autenticado.conta, ContaCorrente):
                print("Limite: ", cliente_autenticado.conta.limite_extra)
            continue
        elif operacao == "sair":
            print("Obrigado por utilizar o banco!")
            break
        else:
            print("Opção inválida")
            continue
else:
    print("Falha na autenticação!")