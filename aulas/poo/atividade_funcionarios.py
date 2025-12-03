# #atividade
class Funcionario:

    def __init__(self, nome_dado, cargo_dado):
        self.nome = nome_dado
        self.cargo = cargo_dado

nome_dado = str(input("Qual o seu nome?"))
cargo_dado = str(input("Qual o cargo do funcionario?"))

funcionario_1 = Funcionario(nome_dado ,cargo_dado)
print('O nome do funcionário é: {}, e o seu cargo é: {}.'.format(funcionario_1.nome, funcionario_1.cargo))
#feito pelo prof
    def calcular_bonus(self):
        #logica de metodo
        #usa o 'Self.salario' (dado exclusivo da instância)

        return self.salario * Funcionario.taxa_bonus

    print('-' *40)
    print('Cadastro de Funcionário (1/2)')
    print('-' *40)

    nome_a = input('Nome do funcionario A: ')
    cargo_a = input('Cargo do funcionario A: '))