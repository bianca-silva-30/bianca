class Aluno:
    def __init__(self, nome, nota):
        #atributo privado (encapsulado)
        self.__nome = nome
        self.__nota = nota

    def get_nome(self):
        return self.__nome

    def get_nota(self):
        return self.__nota

    #Setter: alternar a nota apenas se estiver entre 0 e 10
    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
            print("Nota alterada com sucesso")

        else:
            print("Nota inválida deve ser entre 0 e 10")

aluno = Aluno("Bianca", 10)

aluno.set_nota(15) #nao altera

#acessando os dados via os getters

print("Nome do aluno: ",aluno.get_nome())
print("Nota do aluno: ",aluno.get_nota())
    #Setter: alternar a nota apenas se estiver entre 0 e 10
