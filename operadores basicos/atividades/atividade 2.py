lista_cores = ['azul','verde','amarelo','vermelho']
for cor in lista_cores:
     print(cor)
#for = para
for x in range(1, 11):
     print("Contador:",x)

#while = enquanto
valor = 50
while valor > 0:
    valor = valor - 10
    print(valor)

for i in range(1,21):
    # condicao de pular (continue)
    if i % 3 == 0:
        continue
        # se for divisivel por 3, volta ao inicio
    if i == 17:
        print('Chegamos ao 17. Parando o laço.')
        break
        #condicao para parar BREAK
    print(i)