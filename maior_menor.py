# Programa para ler 3 números, encontrar maior, menor, soma e média

# 1. Leitura dos dados de entrada
# Usa float() para permitir números decimais. input() recebe o texto.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# 2. Processamento: Maior e Menor número
# Inicialmente assumimos que o primeiro número é o maior e o menor.
maior = num1
menor = num1

# Estrutura de decisão para encontrar o MAIOR
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Estrutura de decisão para encontrar o MENOR
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# 3. Processamento: Soma e Média
soma = num1 + num2 + num3
media = soma / 3

# 4. Saída de dados formatada
print("-" * 20)
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")

#:.2f formata a média para 2 casas decimais
print(f"Média: {media:.2f}")
print("-" * 20)