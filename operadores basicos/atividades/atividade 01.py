frequencia = int(input('Digite sua frequencia:'))
media_final = float(input('Digite sua média final:'))
if frequencia >= 75 and media_final >= 7.0:
    print('Você foi aprovado!')
elif frequencia < 75 or (frequencia >= 75) and media_final < 5.0:
    print('Você está reprovado!')
else:
    print('Você está de recuperação!')