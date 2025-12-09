# Atividade
# Você deve criar a classe Aeronave para modelar os dados das aeronaves que estão sendo rastreadas por
# uma torre de controle.
# Atributo de CLASSE (Constante)
# Defina espaco _aereo = "Controlado" - Valor padrão para o ambiente de operação.
# Atribetina total aeronaves = 0 - Contador para saber quantas aeronaves foram cadastradas.
# Método Construtor (Init)Receber prefixo (ex: PR-ABC) e companhia como parâmetros. Inicialização
# da instância.
# Atributos de INSTÂNCIA
# Crie self. prefixo, self.companhia e self altitude = 0 (altitude inicial no solo). -Dados exclusivos de cada
# aeronave.
# Exibição de DadosÃo final, use print() para exibir o prefixo do objeto criado, sua altitude (instância) e o
# total geral de aeronaves (classe). Demonstração do estado inicial dos atributos.

class Aeronave:
    espaco_aereo = "Controlado"
    total_aeronaves = 0
    # prefixo = 'Pr-'

    def __init__(self, prefixo, companhia, altitude):
        self.prefixo = prefixo
        self.companhia = companhia
        self.altitude = altitude

aeronave1 = Aeronave('PR-ABC', 'Latam', "123")
aeronave2 = Aeronave('Gol-123', 'Gol', "456")
aeronave3 = Aeronave('Azul-456', 'Azul', "789")

print(f"Aeronave1:{aeronave1.prefixo} | Companhia: {aeronave1.companhia}"
      f"| Altitude: {aeronave1.altitude}")
print(f"Aeronave2: {aeronave1.prefixo} | Companhia: {aeronave2.prefixo}"
      f"| Altitude: {aeronave2.altitude}")
print(f"Aeronave3: {aeronave1.prefixo} | Companhia: {aeronave3.prefixo}"
      f"| Altitude: {aeronave3.altitude}")
print(f"Total Aeronaves: {Aeronave.total_aeronaves}")

# prefixo = 'Pr-'
# teste = prefixo + "corinthians"
# print(teste)
