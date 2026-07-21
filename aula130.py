# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # recebe o self
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password

    # sempre q o método usar self, ele é um método de instância
    @classmethod # recebe a classe
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print("LOG:", msg)

# ou
def connection_log(msg):
        print("LOG:", msg)

c1 = Connection.create_with_auth("luiz", "123")
# c1.set_user("Luiz")
# c1.set_password("123")
print(Connection.log("Essa é a mensgem de log"))
print(c1.user)
print(c1.password)
