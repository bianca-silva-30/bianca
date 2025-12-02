# #definindo uma variável
# idade = int(input('Qual a sua idade?'))
# if idade >= 18:
#     print('Você é maior de idade')
#     #codigo executado se a condição for verdadeira
# elif 13 <= idade <= 18:
#     print ('Você é adolescente')
#     #codigo executado se o primeiro if der falso
# else:
#     print('Você é menor de idade')
#     #codigo executado se todas as condições anteriores forem falsas

#
# numero = int(input('Digite um número?'))
# if numero > 0 and numero %2 == 0:
#     print('O número positivo é par')
#         # codigo executado se a condição for verdadeira
# elif numero > 0 and numero %2 != 0 :
#     print('O número positivo é impar')
#         # codigo executado se o primeiro if der falso
# else:
#     print('O número é zero ou negativo')
#         # codigo executado se todas as condições anteriores forem falsas
idade = int(input('Qual a sua idade?'))
entrada_carteira = input('Você tem CNH? (sim/não):').lower()
tem_carteira = entrada_carteira == 'sim'
if tem_carteira:
    print('Você é maior de idade e tem CNH. pode dirigir')
        # codigo executado se a condição for verdadeira
# elif numero > 0 and numero %2 != 0 :
#     print('O número positivo é impar')
#         # codigo executado se o primeiro if der falso
else:
    print('Você é maior de idade e não tem CNH. não pode dirigir')
        # codigo executado se todas as condições anteriores forem falsas