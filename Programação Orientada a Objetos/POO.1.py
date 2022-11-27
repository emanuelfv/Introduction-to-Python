#Criando classes
#----Com Parâmetros----
class Carro:
    #atributos
    cor = 'Preto'
    modelo = 'Vivace'
    marca = 'Fiat'
    placa = 'PWA0000'
    #Métodos - funções
    
    #Não fazer nada
print(Carro.cor)
#----Com Parâmetros----
class meuCarro:
    #Método construtor
    def __init__(self, cor, modelo, marca, placa):
        #Atributos
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
    #Método - funções
    def CarroAndando(self,som):
        if som != 'Vruuum':
            print("Seu carro está andando")
        else:
            print("Infelizmente não andou")

    def Marcha(self,machinha):
        if machinha == 1:
            print('Acelera aí!')
        if machinha == 2:
            print('ASsim tá bom!')
        if machinha == 3:
            print('Tá muito rápido')
        else:
            print('Bem que podia ligar né?')
        
#---------INICIO----------
#"Dando nome aos bois", pondo características
CarroUm = meuCarro('Roxo','Sedan','Chevrolet', 'POO085')
print(CarroUm)
#Defini se está andando ou não...
CarroUm.CarroAndando('Vruuum')
#Hora de passar as marchas!
CarroUm.Marcha(2)
