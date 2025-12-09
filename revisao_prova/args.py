n1 = 10
n2 = 20
def soma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

# print(soma(1, 2, 3))      # 6
# print(soma(10, 20))       # 30
# print(soma(4, 7, 1, 9))   # 21
print(soma(n1 + n2))