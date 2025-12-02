def saudacao():
    print("Olá mundo")
saudacao()

#passando valores por parametros
def saudacao(nome):
    print(f"Olá, {nome}")
saudacao("Bianca")

#ela retorna um valor usando uma palavra chamada "return"
def soma(a, b):
    return a + b

resultado =soma(5, 4)
print(resultado)

#função permite retornar multiplos valores usando tupla

def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(10, 3)
print(f"quociente: {q}, resto: {r}") #output 3,1

def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado
#
def soma(*dados):
    resultado = 0
    for num in dados:
        resultado += num
    return resultado

#exemplo de uso
print(soma(1,2,3,4)) #saida: 10
print(soma(10,20)) #saida: 30

def lista_convidados(formatura, *args):
    print(f"Evento: {formatura}")
    if args:  #verifica se a tupla args não está vazia
        print("Convidados:")
    for nome in args:
        print(f"- {nome}")
    else:
        print("Nenhum convidado registrado.")
lista_convidados("Reuniao de equipe", "Marcos", "Alice", "João", "Sofia")
#atividade

def criar_etiqueta_produto(nome_produto, *caracteristicas):
    print(f"\n--- Produto: {nome_produto} ---")
    if caracteristicas:  # verifica se a tupla args não está vazia
        print("Caracteristicas:")
        for item in caracteristicas:
            print(f"- {item}")
    else:
        print("Nenhuma caracteristica adicional registrada")

criar_etiqueta_produto("Smartphone X10", "128GB de armazenamento")
