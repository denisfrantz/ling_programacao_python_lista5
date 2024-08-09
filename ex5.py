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
        
class Administrador(Empregado):
    def __init__ (self, salarioBase, mesesTrabalhados, nome, endereço, ajudasDeCusto):
        super().__init__(nome, endereço, salarioBase, mesesTrabalhados)
        self.ajudasDeCusto = ajudasDeCusto
        
    def setAjudasDeCusto (self, ajudasDeCusto):
        self.ajudasDeCusto = ajudasDeCusto
        
    def getAjudasDeCusto (self):
        return self.ajudasDeCusto
    
    def calcularSalario (self):
        print ("\nSalário total = (", self.salarioBase, "x", self.mesesTrabalhados, ") +", self.ajudasDeCusto)
        print ("Salário total =", round((self.salarioBase * self.mesesTrabalhados) + self.ajudasDeCusto, 2))

print ("Em relação ao administrador, informe os seguintes dados\n")
nome = input("Nome: ")
endereço = input("Endereço: ")
salarioBase = float(input("Salário base: "))
mesesTrabalhados = int(input("Meses trabalhados: "))
ajudasDeCusto = float(input("Ajudas de custo: "))

e1 = Administrador(salarioBase, mesesTrabalhados, nome, endereço, ajudasDeCusto)
e1.setNome(nome)
e1.getNome()

e1.setEndereço(endereço)
e1.getEndereço()

e1.setSalarioBase(salarioBase)
e1.getSalarioBase()
    
e1.setMesesTrabalhados(mesesTrabalhados)
e1.getMesesTrabalhados()    

e1.setAjudasDeCusto(ajudasDeCusto)
e1.getAjudasDeCusto()

e1.calcularSalario()