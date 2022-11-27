class Banco:
    def __init__(self, Boleto, Extrato, Dinheiro):
        self.Boleto = Boleto
        self.Extrato = Extrato
        self.Dinheiro = Dinheiro

    def Pagamento(self, Pagamento):

        if Pagamento >= 25 :
            print('Pagamento bem sucedido!')
        else:
            print(f'Está faltando {self.Boleto - Pagamento} reais')

Inter = Banco(25, 5, 100)
Inter.Pagamento(int(input('Digite o valor do pagamento: ')))
