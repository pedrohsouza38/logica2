# Programa: Exibir números de 1 a 100

def exibir_numeros():
    """
    Função que usa uma estrutura de repetição for
    para imprimir números de 1 até 100.
    """
    
    # O range(1, 101) gera uma sequência de 1 até 100.
    # O segundo parâmetro é exclusivo (para antes dele), portanto, usamos 101 para incluir o 100.
    for numero in range(1, 101):
        # Exibe o número atual da iteração
        print(numero)

# Executa a função
if __name__ == "__main__":
    exibir_numeros()