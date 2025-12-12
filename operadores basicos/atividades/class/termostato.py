class Termostato:
    def __init__(self, temperatura = 20):
        # Atributo da instância
        self.temperatura = temperatura

    # metodo adiciona graus à temperatura
    def aumentar(self, graus):
        self.temperatura += graus
        print(f"Temperatura aumentada para: {self.temperatura}C")

    def diminuir(self, graus):
        self.temperatura -= graus
        print(f"Temperatura reduzida para: {self.temperatura}C")

#teste
meu_termostato = Termostato()
print(f"inicial: {meu_termostato.temperatura}!")
meu_termostato.aumentar(3)
meu_termostato.diminuir(1)
print(f"Temperatura final: {meu_termostato.temperatura}C")