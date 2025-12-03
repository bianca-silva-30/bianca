class Funcionario:

    def __init__(self, nome_dado, cargo_dado, salario_dado,calcular_bonus, taxa_bonus):
        self.nome = nome_dado
        self.cargo = cargo_dado
        self.salario = salario_dado
        self.bonus = calcular_bonus
        self.taxa = taxa_bonus

nome_dado = str(input("Qual o seu nome?"))
cargo_dado = str(input("Qual o cargo do funcionario?"))
salario_dado = float(input("Digite seu salario:"))
taxa_bonus = 0.10
calcular_bonus = salario_dado + (salario_dado * taxa_bonus)

funcionario_1 = Funcionario(nome_dado ,cargo_dado, salario_dado,calcular_bonus,taxa_bonus,)
# print('O nome do funcionário é: {}, e o seu cargo é: {}, e o seu salario com o bonus é: {}.'.format(funcionario_1.nome, funcionario_1.cargo, funcionario_1.bonus))
print('O nome do funcionário é: {}\nSeu cargo é: {}\nO seu salario é: {}\nO salário com o bonus é: {}.'.format(funcionario_1.nome, funcionario_1.cargo,funcionario_1.salario, funcionario_1.bonus))
