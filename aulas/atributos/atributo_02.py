class ContadorDeObjetos:
    #Atributo de classe
    total_objetos = 0

    def __init__(self, nome):
        self.nome = nome

        #Modifica o atributo de Classe
        ContadorDeObjetos.total_objetos += 1

    def exibir_contagem(self):

        print(f'Objeto {self.nome} criado. Ttotal geral: ')
            f'{ContadorDeObjetos.total_objetos}'

#Criação de Objetos e execução do Contador:
objeto_1 = ContadorDeObjetos('Item A')
objeto_1.exibir_contagem()
#saída: Objeto 'Item A' criado. Total geral = 1.

objeto_2 = ContadorDeObjetos('Item B')
objeto_2.exibir_contagem()
#saída: Objeto 'Item B' criado. Total geral = 2.

#objeto 1 e 2 compartilham o mesmo contador