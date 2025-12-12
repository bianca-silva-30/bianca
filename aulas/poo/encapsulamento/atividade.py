class Produto:

    def __init__(self, preco):

        self.__preco = preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco += valor

        else:
            print("Valor inválido!")

    def get_preco(self):
        return self.__preco

# produto = Produto(100)
preco_produto = input("Qual o preço do produto? ")
produto = Produto(preco_produto)

#Tentando alterar preço para o valor negativo
produto.set_preco(-50)
#mostrar o preço usando o getter
print("Preço atual:", produto.get_preco())


