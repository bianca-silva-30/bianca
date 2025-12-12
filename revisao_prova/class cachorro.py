class Cachorro:

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self. idade = idade
#
# nome = input('Qual o nome do seu cachorro?')
# raca = input('Qual a raça do seu cachorro?')
# idade = input('Qual a idade do seu cachorro?')

    # metodo: comportamento/acao
    def latir(self):
        return f'{self.nome} o cachorro está latindo: AU AU'

    #metodo que modifica o estado do objeto
    def fazer_aniversario(self):
        self.idade += 1 #modifica o atributo idade
        return f'Parabéns! {self.nome} agora tem {self.idade} anos!'

    #metodo: comportamento que usa multiplos atributos
    def apresentar(self):
        return f'Olá,eu sou {self.nome} um {self.raca} e tenho {self.idade} anos!'
dog_a = Cachorro('Max', 'Golden Retriver', 5)
dog_b = Cachorro('Luna', "Lulu da Pomerania", 6)

print(dog_a.apresentar())
print(dog_a.latir())
print(dog_a.fazer_aniversario())

print(dog_b.apresentar())
print(dog_b.latir())
print(dog_b.fazer_aniversario())

#alterando o estado do max atraves de um metodo
print(dog_a.fazer_aniversario())
print(dog_a.apresentar()) #verifica a idade atualizada