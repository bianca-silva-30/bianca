class Personagem: #SuperClasse (classe mãe)
    def __init__ (self, nome, vida):
        self.nome = nome
        self.vida = vida

class Heroi(Personagem): #Subclasse (classe filho)
    def __init__ (self, nome, vida, habilidade):
        super().__init__(nome,vida)
        self.habilidade = habilidade

class Vilao(Personagem):
    def __init__(self,nome,vida,poder):
        super().__init__(nome,vida)
        self.poder = poder

def atacar(personagem):
    print(f"{personagem.nome} está atacando")

nome_heroi = input("Qual o nome do seu Heroi? ")
vida_heroi = int(input(f"Qual a vida do {nome_heroi}? "))
habilidade_heroi = input(f"Qual a habilidade do {nome_heroi}? ")

heroi1 = Heroi(nome_heroi, vida_heroi, habilidade_heroi)

nome_vilao = input("\nQual o nome do seu Vilão? ")
vida_vilao = int(input(f"Qual a vida do {nome_vilao}? "))
habilidade_vilao = input(f"Qual a habilidade do {nome_vilao}? ")

vilao1 = Vilao(nome_vilao, vida_vilao, habilidade_vilao)

atacar(heroi1)
atacar(vilao1)