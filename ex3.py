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
    def __init__ (self, salarioBase, mesesTrabalhados, nome, endereço):
        super().__init__(nome, endereço)
        self.salarioBase = salarioBase
        self.mesesTrabalhados = mesesTrabalhados
    
    def setSalarioBase (self, salarioBase):
        self.salarioBase = salarioBase
    
    def getSalarioBase (self):
        return self.salarioBase
    
    def setMesesTrabalhados (self, mesesTrabalhados):
        self.mesesTrabalhados = mesesTrabalhados
        
    def getMesesTrabalhados (self):
        return self.mesesTrabalhados
    
    def calcularSalario (self):
        print ("\nSalário total =", self.salarioBase, "x", self.mesesTrabalhados)
        print ("Salário total =", round(self.salarioBase * self.mesesTrabalhados, 2))

print ("Em relação ao empregado, informe os seguintes dados\n")
nome = input("Nome: ")
endereço = input("Endereço: ")
salarioBase = float(input("Salário base: "))
mesesTrabalhados = int(input("Meses trabalhados: "))

e1 = Empregado(salarioBase, mesesTrabalhados, nome, endereço)
e1.setNome(nome)
e1.getNome()

e1.setEndereço(endereço)
e1.getEndereço()

e1.setSalarioBase(salarioBase)
e1.getSalarioBase()
    
e1.setMesesTrabalhados(mesesTrabalhados)
e1.getMesesTrabalhados()    

e1.calcularSalario()