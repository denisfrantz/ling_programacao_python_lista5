class Pessoa:
    def __init__ (self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def setNome (self, nome):
        self.nome = nome
        
    def setEndereço (self, endereco):
        self.endereco = endereco
    
    def getNome (self):
        return self.nome
    
    def getEndereço (self):
        return self.endereco