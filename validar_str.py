# --- Programa para validação de string em branco ---

def main():
    # 1. Entrada de dados
    # A função input() recebe o texto do usuário.
    # Usamos strip() para remover espaços em branco desnecessários no início/fim.
    entrada = input("Digite algo: ").strip()

    # 2. Estrutura de Decisão (if/else)
    # Justificativa: Necessária para verificar se a string está vazia após o strip().
    # if not entrada: verifica se a string é falsa (vazia "" ou apenas espaços)
    
    if not entrada:
        # Se for vazio, exibe a mensagem de erro
        print("Dado inválido")
    else:
        # Se contiver conteúdo, exibe o valor digitado
        print(f"Você digitou: {entrada}")

# Executa o programa
if __name__ == "__main__":
    main()