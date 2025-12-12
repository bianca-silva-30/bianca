class Conta:

    def __init__(self):

        #Atributo privado: só pode ser acessado dentro da classe
        self.__saldo = 0

    #GETTER -> utilizado para ler um atributo privado
    #permite acessar o valor sem alterar diretamente
    def get_saldo(self):
        return self.__saldo

    #SETTER -> altera o atributo privado mas de forma controlada
    #aqui ele funciona como um SETTER, mas com o nome "depositar"
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor


#exemplo de uso

conta = Conta()

print(conta.get_saldo())

# conta.depositar(500)
conta.depositar = float(input('Qual o valor que você deseja depositar? '))

# conta.sacar(200)
conta.sacar = float(input("Qual o valor que você deseja sacar? "))

#verificar novamente o saldo da conta via GETTER
print(conta.get_saldo())

print('saldo usando o GETTER:', conta.get_saldo())

# print(conta.__saldo)