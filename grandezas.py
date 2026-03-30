# PROGRAMA: Calculadora de Grandezas Elétricas (Lei de Ohm)
# OBJETIVO: Auxiliar eletricistas nos cálculos de Tensão, Resistência e Corrente.

def mostrar_menu():
    """Exibe o menu principal de opções."""
    print("\n--- CÁLCULO DE GRANDEZAS ELÉTRICAS ---")
    print("1. Tensão (em Volt - U = R * I)")
    print("2. Resistência (em Ohm - R = U / I)")
    print("3. Corrente (em Ampére - I = U / R)")
    print("4. Sair do programa")
    print("--------------------------------------")

def calculadora():
    # Estrutura de repetição 'while True' para manter o menu ativo
    while True:
        mostrar_menu()
        opcao = input("Qual grandeza deseja calcular? (1-4): ")

        # --- ESTRUTURAS DE DECISÃO (if/elif/else) ---
        # A estrutura de decisão é fundamental aqui para direcionar o fluxo do programa baseada estritamente na escolha do usuário.

        if opcao == '1':
            # Cálculo de Tensão: U = R * I
            print("\n>> Cálculo de Tensão (U)")
            try:
                r = float(input("Informe o valor da Resistência (Ohm): "))
                i = float(input("Informe o valor da Corrente (Ampére): "))
                u = r * i
                print(f"Resultado: Tensão = {u:.2f} V")
            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos.")

        elif opcao == '2':
            # Cálculo de Resistência: R = U / I
            print("\n>> Cálculo de Resistência (R)")
            try:
                u = float(input("Informe o valor da Tensão (Volt): "))
                i = float(input("Informe o valor da Corrente (Ampére): "))
                # Estrutura de decisão aninhada para evitar divisão por zero
                if i != 0:
                    r = u / i
                    print(f"Resultado: Resistência = {r:.2f} Ώ")
                else:
                    print("Erro: A corrente não pode ser zero.")
            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos.")

        elif opcao == '3':
            # Cálculo de Corrente: I = U / R
            print("\n>> Cálculo de Corrente (I)")
            try:
                u = float(input("Informe o valor da Tensão (Volt): "))
                r = float(input("Informe o valor da Resistência (Ohm): "))
                # Estrutura de decisão aninhada para evitar divisão por zero
                if r != 0:
                    i = u / r
                    print(f"Resultado: Corrente = {i:.2f} A")
                else:
                    print("Erro: A resistência não pode ser zero.")
            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos.")

        elif opcao == '4':
            print("Encerrando o programa... Até logo!")
            break # Encerra o loop e sai do programa
        
        else:
            # Caso o usuário digite qualquer coisa diferente de 1, 2, 3 ou 4
            print("Opção inválida! Tente novamente.")

# Executa a calculadora
if __name__ == "__main__":
    calculadora()