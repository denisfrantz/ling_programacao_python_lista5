class Pessoa:
    def __init__ (self, nome, endereço):
        self.nome = nome
        self.endereço = endereço
    
    def setNome (self, nome):
        self.nome = nome
    
    def setEndereço (self, endereço):
        self.endereço = endereço
    
    def getNome (self):
        return self.nome
    
    def getEndereço (self):
        return self.endereço
    
class Cliente(Pessoa):
    def __init__ (self, credimaximo, valorEmDivida, nome, endereço):
        super().__init__(nome, endereço)
        self.credimaximo = credimaximo
        self.valorEmDivida = valorEmDivida
    
    def setCredimaximo (self, credimaximo):
        self.credimaximo = credimaximo
    
    def setValorEmDivida (self, valorEmDivida):
        self.valorEmDivida = valorEmDivida
    
    def getCredimaximo (self):
        return self.credimaximo
        
    def getValorEmDivida (self):
        return self.valorEmDivida
    
    def obterSaldo (self):
        print ("\nSaldo =", self.credimaximo, "-",  self.valorEmDivida)
        print ("Saldo =", round(self.credimaximo - self.valorEmDivida, 2))

print ("Em relação ao cliente, informe os seguintes dados\n")
nome = input("Nome: ")
endereço = input("Endereço: ")
credimaximo = float(input("Crédito máximo: "))
valorEmDivida = float(input("Valor em dívida: "))

f1 = Cliente(credimaximo, valorEmDivida, nome, endereço)
f1.setNome(nome)
f1.getNome()

f1.setEndereço(endereço)
f1.getEndereço()

f1.setCredimaximo(credimaximo)
f1.getCredimaximo()
    
f1.setValorEmDivida(valorEmDivida)
f1.getValorEmDivida()    

f1.obterSaldo()