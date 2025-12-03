class Carro:
    #Atributo da classe
    roda = 4

    def __init__(self , marca, modelo):
        self.marca = marca #atributo de instancia
        self.modelo = modelo #atributo de instancia

carro_a = Carro('Honda','Civic')

#estamos acessando pelo Objeto(Instãncia)
print('Seu carro é da marca {}, e o seu modelo é: {}.'.format(carro_a.marca, carro_a.modelo))
#Saída: O Civic tem 4 rodas

print(f'Todo Carro deve ter {Carro.roda} rodas')
#Saída: Todod Carro deve ter 4 rodas

Carro.roda = 6
print(f'Novo valor em carro_a: {carro_a.roda}')
