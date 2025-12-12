# class Tarefa:
#     def __init__(self,descricao,concluida):
#         self.descricao = descricao
#         self.concluida = False
#
#     def marcar_concluida(self):
#         self.concluida = True
#         print(f"Tarefa: {self.descricao} marcada como Concluída")
#
# tarefa_py = Tarefa('Aprender Métodos em Python')
# tarefa_py.marcar_concluida()
# print(f"Sua tarefa foi {tarefa_py.marcar_concluida}")

# questao 3
class Nave:

    def __init__ (self, nome,combustivel, status = "Estacionada"):
        self.nome = nome
        self.combustivel = combustivel
        self.status = status

    def recarregar(self):
        self.recarregar += self.combustivel
        print(f"Combustível após a recarga: {self.recarregar}")

    def decolar(self):
        self.decolar = self.combustivel - 20
        print(f"Combustível restante após a decolagem: {self.decolar}")