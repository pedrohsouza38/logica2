# Solução de Radar Eletrônico em Python

# 1. Solicita a velocidade ao usuário e converte para número decimal (float)
velocidade = float(input("Digite a velocidade do seu carro (Km/h): "))

# Define o limite de velocidade
limite = 80

# 2. Estrutura de Decisão: Verifica se a velocidade é maior que 80 km/h
if velocidade > limite:
    # Calcula a diferença entre a velocidade atual e o limite
    km_excedido = velocidade - limite
    
    # Calcula o valor da multa: R$ 50,00 por km acima do limite
    valor_multa = km_excedido * 50.00
    
    # Exibe a mensagem de multa e o valor formatado (2 casas decimais)
    print(f"Você foi multado! A velocidade excedeu em {km_excedido:.1f} Km/h.")
    print(f"Valor da multa: R$ {valor_multa:.2f}")

else:
    # Caso a velocidade seja 80 ou menos
    print("Velocidade dentro do limite. Boa viagem!")