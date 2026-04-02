import time  # Importa o módulo time para usar a função sleep (pausa)

def contagem_regressiva():
    """
    Simula uma contagem regressiva de 10 a 0 e lança o foguete.
    """
    print("Iniciando contagem regressiva...")
    
    # Estrutura de repetição 'for' com range decrescente
    # range(início, fim, passo) -> vai de 10 até 0 (o fim é exclusivo)
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # Pausa a execução por 1 segundo
    
    # Estrutura de decisão para verificar se a contagem terminou
    # Em um cenário real, aqui verificaríamos se o número é 0
    motor_ligado = True
    if motor_ligado:
        print("Ignição!")

# Chama a função principal
if __name__ == "__main__":
    contagem_regressiva()