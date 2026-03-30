# Sistema de Validação de Acesso - Rede SENAI-SP

# 1. Definição dos dados de login válidos (Dados do exercício)
# Login 1: atila / 12345
# Login 2: olivi / 54321
user1, pass1 = "atila", "12345"
user2, pass2 = "olivi", "54321"

# 2. Entrada de dados
# O programa solicita que o usuário insira seu login e senha
print("--- Login SENAI-SP ---")
usuario_input = input("Usuário: ")
senha_input = input("Senha: ")

# 3. Estrutura de Decisão (Validação)
# Verifica se o par informado corresponde a algum dos logins cadastrados.
# O operador 'or' permite a validação dos dois pares de usuários distintos.
if (usuario_input == user1 and senha_input == pass1) or \
   (usuario_input == user2 and senha_input == pass2):
    # Se uma das condições for verdadeira, o acesso é garantido
    print("Seja bem vindo!")
else:
    # Se nenhuma for verdadeira, o acesso é negado
    print("Usuário e senha não conferem")