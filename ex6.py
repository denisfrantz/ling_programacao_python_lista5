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

class Empregado(Pessoa):
    def __init__ (self, nome, endereço, salarioBase, mesesTrabalhados):
        super().__init__(nome, endereço)
        self.salarioBase = salarioBase
        self.mesesTrabalhados = mesesTrabalhados
    
    def setSalarioBase (self, salarioBase):
        self.salarioBase = salarioBase
    
    def setMesesTrabalhados (self, mesesTrabalhados):
        self.mesesTrabalhados = mesesTrabalhados
    
    def getSalarioBase (self):
        return self.salarioBase
        
    def getMesesTrabalhados (self):
        return self.mesesTrabalhados
    
    def calcularSalario (self):
        return self.salarioBase * self.mesesTrabalhados
        
class Operario(Empregado):
    def __init__ (self, salarioBase, mesesTrabalhados, nome, endereço, valorProdução, comissão):
        super().__init__(nome, endereço, salarioBase, mesesTrabalhados)
        self.valorProdução = valorProdução
        self.comissão = comissão
    
    def setValorProdução (self, valorProdução):
        self.valorProdução = valorProdução
        
    def getValorProdução (self):
        return self.valorProdução
        
    def setComissão (self, comissão):
        self.comissão = comissão
        
    def getComissão (self):
        return self.comissão
        
    def calcularSalario (self):
        print ("\nSalário total = (", self.salarioBase, "x", self.mesesTrabalhados, ") +", self.comissão) 
        print ("Salário total =", (self.salarioBase * self.mesesTrabalhados) + self.comissão)

print ("Em relação ao operário, informe os seguintes dados\n")
nome = input("Nome: ")
endereço = input("Endereço: ")
salarioBase = float(input("Salário base: "))
mesesTrabalhados = int(input("Meses trabalhados do Operário: "))
valorProdução = float(input("Valor de produção: "))
comissão = float(input("Comissão: "))

e1 = Operario(salarioBase, mesesTrabalhados, nome, endereço, valorProdução, comissão)
e1.setNome(nome)
e1.getNome()

e1.setEndereço(endereço)
e1.getEndereço()

e1.setSalarioBase(salarioBase)
e1.getSalarioBase()
    
e1.setMesesTrabalhados(mesesTrabalhados)
e1.getMesesTrabalhados()    

e1.setValorProdução(valorProdução)
e1.getValorProdução()

e1.setComissão(comissão)
e1.getComissão()

e1.calcularSalario()