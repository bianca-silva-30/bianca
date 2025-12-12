class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz som generico.")

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome,especie)
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} está latindo: au au!")

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Especie: {self.especie} | Raça: {self.raca}")

class Gato(Animal):
    def __init__(self, nome, especie, raca, cor_pelo):

        super().__init__(nome,especie)

        self.raca = raca
        self.cor_pelo = cor_pelo

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} está miando: miau miau!")

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Especie: {self.especie} | Raça: {self.raca} | Cor do pelo: {self.cor_pelo}")

#doguinho = Cachorro("Ducky", "Canino", "Golden Retriver")

nome_doguinho = input("Qual o nome do seu cahorro? ")
especie_doguinho = (input(f"Qual a especie do {nome_doguinho}? "))
raca_doguinho = input(f"Qual a raça do {nome_doguinho}? ")

doguinho = Cachorro(nome_doguinho, especie_doguinho, raca_doguinho)
print(f"Nome herdado: {doguinho.nome}")
doguinho.fazer_som()
doguinho.mostrar_detalhes()

nome_gatinho = input("Qual o nome do seu Gato? ")
especie_gatinho = (input(f"Qual a especie do {nome_gatinho}? "))
raca_gatinho = raca_doguinho = input(f"Qual a raça do {nome_gatinho}? ")
cor_pelo_gatinho = input(f"Qual a cor do pelo do {nome_gatinho}? ")
gatinho = Gato(nome_gatinho, especie_gatinho, raca_gatinho, cor_pelo_gatinho)

print(f"Nome herdado: {gatinho.nome}")
gatinho.fazer_som()
gatinho.mostrar_detalhes()
