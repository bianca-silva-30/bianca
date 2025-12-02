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
