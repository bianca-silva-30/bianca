inteiro = 10
decimal = 10.5
complexo = 3 + 4j

print(inteiro, decimal, complexo)
print(f'Tipos: {type(inteiro)}, {type(decimal)}, {type(complexo)}')

#texto
texto = 'Bianca'
print(texto)
print(f'Tipos: {type(texto)}')

#booleanos
verdadeiro = True
falso = False
print(verdadeiro, falso)
print(f'tipo: {type(verdadeiro)}, {type(falso)}')

# coleções
lista = [1,2,3] # (lista mutável)
tupla = (1,2,3) # (tupla imutável)
dicionario = {'nome': 'Bianca'} #dict (dicionário)
conjunto = {1,2,3} #set (conjunto)
print(lista)
print(tupla)
print(dicionario)
print(f'tipo: {type(lista)}, {type(tupla)}, {type(dicionario)}')
