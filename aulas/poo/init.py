# class Livro:
#     pass
class Livro:

    #O montador da Fábrica (Construtor)
    def __init__(self, titulo_dado, autor_dado):
        #A magia acontece pq os atributos sao iniciados
        self.titulo = titulo_dado
        self.autor = autor_dado

    def exibir_info(self):
        print(f'Livro cadastrado: {self.titulo} - {self.autor}')

print('-'*40)
print('Cadastro de novo livro (1/2)')
print('-'*40)

titulo_a = input('Digite o titulo do livro A: ')
autor_a = input('Digite o autor do livro A: ')

livro_a = Livro(titulo_a, autor_a)

print('-'*40)
print('Cadastro de novo livro (2/2)')
print('-'*40)

titulo_b = input('Digite o titulo do livro B: ')
autor_b = input('Digite o autor do livro B: ')

livro_b = Livro(titulo_b, autor_b)

print('\n' + '-'*40)
print('Verificação final: o poder do"SELF"')
print('-'*40)

livro_a.exibir_info()
livro_b.exibir_info()

print('\n --- Acessando atributos Diretamente ---')
print(f'titulo no Objeto A: {livro_a.titulo}')
print(f'titulo no Objeto B: {livro_b.titulo}')