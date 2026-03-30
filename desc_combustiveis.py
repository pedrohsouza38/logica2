# Entrada de dados: Litros e Tipo de Combustível
litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Definição de preços base
preco_gasolina = 4.95
preco_alcool = 2.89

# Estrutura de decisão para determinar o valor final
if tipo == 'A':
    # Regras para Álcool
    if litros <= 20:
        desconto = 0.03  # 3% de desconto
    else:
        desconto = 0.05  # 5% de desconto
    
    valor_total = litros * preco_alcool * (1 - desconto)

elif tipo == 'G':
    # Regras para Gasolina
    if litros <= 20:
        desconto = 0.04  # 4% de desconto
    else:
        desconto = 0.06  # 6% de desconto
    
    valor_total = litros * preco_gasolina * (1 - desconto)

else:
    # Caso o usuário digite um código inválido
    valor_total = None
    print("Tipo de combustível inválido!")

# Exibição do resultado
if valor_total is not None:
    print(f"Valor a ser pago: R$ {valor_total:.2f}")