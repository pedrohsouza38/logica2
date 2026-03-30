# Programa para receber um inteiro e validar se o campo está em branco

# 1. Entrada de dados: Recebe a entrada como string primeiro
# O .strip() remove espaços em branco extras antes e depois do texto
entrada = input("Digite um número inteiro: ").strip()

# 2. Estrutura de Decisão: Verifica se a string está vazia
if entrada == "":
    # Se for em branco, exibe a mensagem de erro
    print("Dado inválido")
else:
    # Se não for em branco, tenta converter e exibir
    try:
        # Tenta converter a string para inteiro
        numero = int(entrada)
        print(f"O número digitado foi: {numero}")
    except ValueError:
        # Caso o usuário digite texto (ex: "abc") em vez de um número
        print("Dado inválido")