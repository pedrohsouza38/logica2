# Programa para cálculo de desconto - Black Friday
# Solicita o preço total da venda
preco_total = float(input("Digite o valor total da venda (R$): "))

# Exibe as opções de pagamento para o operador
print("\nCÓDIGO | CONDIÇÃO DE PAGAMENTO | DESCONTO")
print("1      | À vista (espécie)     | 10%")
print("2      | Cartão de débito      | 5%")
print("3      | Cartão de crédito     | 3%")
print("4      | PIX                   | 7.5%")

# Solicita o código da forma de pagamento
codigo = int(input("\nDigite o código da forma de pagamento: "))

# Estrutura de decisão para definir o percentual de desconto
if codigo == 1:
    desconto = 10.0
elif codigo == 2:
    desconto = 5.0
elif codigo == 3:
    desconto = 3.0
elif codigo == 4:
    desconto = 7.5
else:
    desconto = 0.0
    print("Código inválido! Nenhum desconto será aplicado.")

# Cálculo do valor final
# A fórmula aplicada é: Valor * (1 - Porcentagem/100)
valor_final = preco_total * (1 - desconto / 100)

# Exibe o resultado final formatado com duas casas decimais
print(f"\nDesconto aplicado: {desconto}%")
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")