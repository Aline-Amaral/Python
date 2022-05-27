# 8. Classe Bomba de Combustível: Faça um programa completo utilizando classes e
# métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro
# iii. quantidadeCombustivel

class bombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
# b. Possua no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e
# mostra a quantidade de litros que foi colocada no veículo

    def abastecerPorValor(self, valorAbastecido):
        quantidadeLitros = valorAbastecido / self.valorLitro
        print(f"Foram abastecidos {quantidadeLitros} litros de combustível")
        
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
# combustível e mostra o valor a ser pago pelo cliente.

    def abastecerPorLitro(self, quantidadeLitros):
        valorAbastecimento = quantidadeLitros * self.valorLitro
        print(f"O valor a ser pago é R${valorAbastecimento}")

# iii. alterarValor( ) – altera o valor do litro do combustível.

    def alterarValor(self, novoValorLitro):
        self.valorLitro = novoValorLitro
        print(f"O novo valor do litro de combustível é R${self.valorLitro}")

# iv. alterarCombustivel( ) – altera o tipo do combustível.

    def alterarCombustivel(self, novoTipoCombustivel):
        self.tipoCombustivel = novoTipoCombustivel
        print(f"O novo tipo de combustível é: {self.tipoCombustivel}")

# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível
# restante na bomba.

    def alterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        self.quantidadeCombustivel = novaQuantidadeCombustivel
        print(f"A nova quantidade de combustível é: {self.quantidadeCombustivel}")
        

bomba = bombaCombustível('diesel', 3, 450)

bomba.abastecerPorValor(30)

bomba.abastecerPorLitro(15)

bomba.alterarValor(5)

bomba.alterarCombustivel('gasolina')

bomba.alterarQuantidadeCombustivel(400)