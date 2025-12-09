# def soma(*args):
#     total = 0
#     for numero in args:
#         total += 1
#     return total
# print(total())
#4 questao
def calcular_combustivel(missoes_base, *gastos_adicionais):
    combustivel_base = missoes_base * 100

    total_adicional = 0
    for gasto in gastos_adicionais:
        total_adicional += gasto

    total_geral = combustivel_base + total_adicional
    print(f'total de combustivel necessário: {total_geral}')

calcular_combustivel(2,50,25,10)

# output = 285


