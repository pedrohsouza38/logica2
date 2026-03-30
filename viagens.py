# Solicita a distância ao usuário e converte para número de ponto flutuante (float)
distancia = float(input("Digite a distância da viagem em km: "))

# Estrutura condicional para determinar a tarifa
if distancia <= 200:
    # Se a distância for até 200km, o preço é 0.50 por km
    preco = distancia * 0.50
else:
    # Para viagens acima de 200km, o preço é 0.45 por km
    preco = distancia * 0.45

# Exibe o resultado formatado com duas casas decimais
print(f"O preço da passagem é: R$ {preco:.2f}")