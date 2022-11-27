class doggynho():
    def __init__(self, raça, cor):
    #atributos
        self.raça = raça
        self.cor = cor
        
    def Moradia(self, Rua, Bairro, Cidade):
        self.Rua = Rua
        self.Bairro = Bairro
        self.Cidade = Cidade
        print(f'Eu moro em {Cidade} no bairro {Bairro} na rua {Rua}')

    def latir(self,late):
        if late == True:
            print('Au Au!')
        else:
            print('...')

cachorrinho = doggynho('Dalmata', 'Branco') 
cachorrinho.Moradia('Santos Dumond', 'Aldeota', 'Fortaleza')
cachorrinho.latir(True)
