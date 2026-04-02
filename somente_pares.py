# Programa para exibir números pares de 1 a 100
# Utiliza uma estrutura de repetição e uma de decisão

print("Números pares de 1 a 100:")

# 'for' itera sobre a sequência de números de 1 até 100
# O 'range(1, 101)' gera números começando em 1 até 100 (o 101 não é incluído)
for numero in range(1, 101):
    
    # Estrutura de Decisão (if):
    # Verifica se o resto da divisão do número por 2 é igual a zero (par)
    if numero % 2 == 0:
        # Se a condição for verdadeira, o número é par e exibido
        print(numero)

# Alternativa mais eficiente (sem if):
# for numero in range(2, 101, 2):
#     print(numero)