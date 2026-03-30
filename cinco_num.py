# Programa: Leitura e Exibição de 5 Números
# Linguagem: Python
# IDE: Visual Studio Code

def main():
    # Inicializa uma lista vazia para armazenar os números
    numeros = []

    print("--- Digite 5 números ---")

    # ESTRUTURA DE REPETIÇÃO (Loop for)
    # Justificativa: Ideal para executar um bloco de código um número definido de vezes (5).
    # O range(5) gera um iterador de 0 a 4, totalizando 5 repetições.
    for i in range(5):
        # ESTRUTURA DE DECISÃO/TRATAMENTO (Try-Except)
        # Justificativa: Evita que o programa trave se o usuário digitar letras em vez de números.
        try:
            # Lê o número do usuário e converte para float (para aceitar decimais)
            valor = float(input(f"Digite o {i+1}º número: "))
            numeros.append(valor) # Adiciona o número à lista
        except ValueError:
            # Caso ocorra um erro de valor, exibe uma mensagem
            print("Entrada inválida! Por favor, digite um número.")
            # O 'continue' ignora o resto do loop e tenta novamente a mesma iteração
            continue

    # Exibe os números lidos
    print("\n--- Números Digitados ---")
    
    # Percorre a lista e exibe cada número
    for n in numeros:
        print(n)

# Executa a função principal
if __name__ == "__main__":
    main()