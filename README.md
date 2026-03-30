# logica2
Exercícios de Lógica com Python 2

1. Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
Exemplo: Digite a velocidade em Km/h: 85
Limite = 80Km/h
Excedeu 5Km/h
multa = 5Km/h * R$ 50,00
Valor da multa: R$ 250,00
Salvar o código como: multa.py

Solução de Radar Eletrônico em Python

Solicita a velocidade ao usuário e converte para número decimal (float)

velocidade = float(input("Digite a velocidade do seu carro (Km/h): "))

Define o limite de velocidade

limite = 80

Estrutura de Decisão: Verifica se a velocidade é maior que 80 km/h

if velocidade > limite:

    Calcula a diferença entre a velocidade atual e o limite
    
    km_excedido = velocidade - limite
    
    Calcula o valor da multa: R$ 50,00 por km acima do limite
    
    valor_multa = km_excedido * 50.00
    
    Exibe a mensagem de multa e o valor formatado (2 casas decimais)
    
    print(f"Você foi multado! A velocidade excedeu em {km_excedido:.1f} Km/h.")
    print(f"Valor da multa: R$ {valor_multa:.2f}")

else:

    # Caso a velocidade seja 80 ou menos
    
    print("Velocidade dentro do limite. Boa viagem!")

    Justificativa da Estrutura de Decisão
    
A estrutura if / else (se/senão) é crucial neste programa pois ele precisa reagir de forma diferente a situações distintas. 

Avaliação Condicional: O computador compara velocidade > 80.

Fluxo de Controle: Se a condição for verdadeira, ele executa o bloco de código de cálculo da multa.

Alternativa: Se a condição for falsa (velocidade menor ou igual a 80), ele pula o cálculo e executa o bloco else (caso exista), garantindo que apenas infratores sejam multados e evitando cálculos desnecessários para motoristas dentro da lei. 

2. Desenvolva um programa que leia três números e que imprima:
   2.1. o maior,
   2.2. o menor,
   2.3. a soma,
   2.4. a média.
Exemplo:
num1 = 5	num2 = 3	num3 = 10
**********
maior = 10
menor = 3
soma = 18
media = 6
Salvar o código como: maior_menor.py

Programa para ler 3 números, encontrar maior, menor, soma e média

Leitura dos dados de entrada

Usa float() para permitir números decimais. input() recebe o texto.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

Processamento: Maior e Menor número

Inicialmente assumimos que o primeiro número é o maior e o menor.

maior = num1
menor = num1

Estrutura de decisão para encontrar o MAIOR

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

Estrutura de decisão para encontrar o MENOR

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

Processamento: Soma e Média

soma = num1 + num2 + num3
media = soma / 3

Saída de dados formatada

print("-" * 20)
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")

#:.2f formata a média para 2 casas decimais

print(f"Média: {media:.2f}")
print("-" * 20)

Justificativa/Explicação do Uso das Estruturas de Decisão (if)

As estruturas de decisão (if) são cruciais neste algoritmo porque os números digitados pelo usuário podem estar em qualquer ordem. Não podemos assumir qual número é o maior ou o menor de antemão. 

Encontrar o Maior (if num2 > maior):

O código assume inicialmente que o num1 é o maior (maior = num1).

A estrutura if verifica se num2 é maior que o valor atualmente armazenado em maior. Se for verdade, a variável maior é atualizada com o valor de num2.

O processo se repete para num3. Isso garante que, no final, a variável maior contenha o valor máximo.

Encontrar o Menor (if num2 < menor):

Da mesma forma, o código assume num1 como o menor.

A estrutura if compara se num2 é menor que menor. Se sim, a variável menor é atualizada. 

3. Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
Salvar o código como: viagens.py

Solicita a distância ao usuário e converte para número de ponto flutuante (float)

distancia = float(input("Digite a distância da viagem em km: "))

Estrutura condicional para determinar a tarifa

if distancia <= 200:

    # Se a distância for até 200km, o preço é 0.50 por km
    
    preco = distancia * 0.50
    
else:

    # Para viagens acima de 200km, o preço é 0.45 por km
    
    preco = distancia * 0.45

Exibe o resultado formatado com duas casas decimais

print(f"O preço da passagem é: R$ {preco:.2f}")

Justificativa e Explicação das Estruturas

O programa utiliza uma Estrutura Condicional Composta (if e else) para processar a lógica de negócio. Abaixo, o funcionamento de cada etapa:

Entrada de Dados e Tipagem

Utiliza float(input()) porque a distância pode ser um número decimal. O Python, por padrão, recebe entradas como texto (string), por isso a conversão é obrigatória para realizar cálculos matemáticos.

A Condição if distancia <= 200

Esta é a expressão lógica. O programa verifica se o valor armazenado na variável é menor ou igual ao limite de 200 km.

Se verdadeiro: O bloco de código identado logo abaixo é executado, aplicando a taxa de R$ 0,50.

Se falso: O programa ignora esse bloco e passa para a próxima instrução.

O Desvio else

A cláusula else (senão) serve como um caminho alternativo obrigatório quando a condição do if não é atendida. Como qualquer valor que não seja "até 200" será obrigatoriamente "maior que 200", não precisa de um novo teste lógico (como um elif). Isso torna o código mais eficiente e limpo. 

Formatação de Saída

No comando print, utiliza uma f-string com o modificador :.2f. Isso garante que o valor monetário seja exibido com duas casas decimais após o ponto, seguindo o padrão de representação de moedas.

4. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
que são Tensão, Resistência e Corrente. Sabe-se que:
U = R * I, 
onde, 
U é a Tensão      (em V), 
R é a Resistência (em Ώ) e,
I é a Corrente    (em A).

Você foi contratado(a) pela empresa para atender a essa solicitação.
Construa um programa que apresente o seguinte menu:

CÁLCULO DE GRANDEZAS ELÉTRICAS

Tensão (em Volt)
Resistência (em Ohm)
Corrente (em Ampére)
Sair do programa

Qual grandeza deseja calcular?

Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo.

Quando o eletricista escolher:
Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente.
   Utilizar a fórmula: U = R * I

Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente.
   Utilizar a fórmula: R = U / I

Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência.
   Utilizar a fórmula: I = U / R

Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
Obs.: Qualquer opção diferente das apresentadas no menu deverão ser informadas ao usuário como 'Opção inválida!'
Salvar o código como: grandezas.py

PROGRAMA: Calculadora de Grandezas Elétricas (Lei de Ohm)

OBJETIVO: Auxiliar eletricistas nos cálculos de Tensão, Resistência e Corrente.

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

Executa a calculadora

if __name__ == "__main__":
    calculadora()

Justificativa das Estruturas de Decisão (if, elif, else)

As estruturas de decisão (if, elif, else) foram essenciais neste programa para:

Direcionamento de Fluxo (Menu): O programa precisa escolher um caminho de cálculo baseado no número digitado. O if verifica a primeira opção, e os elif (else if) verificam as subsequentes (2, 3) até a saída (4).

Validação de Entrada: O bloco else final captura qualquer entrada que não seja 1, 2, 3 ou 4, garantindo que o programa apresente "Opção inválida!" conforme solicitado, em vez de fechar ou erro.

Tratamento de Exceções Físicas (Divisão por Zero): Dentro das opções de Resistência e Corrente, usamos if i != 0 ou if r != 0. Isso é uma estrutura de decisão fundamental na engenharia, pois, matematicamente, dividir por zero causa um erro no programa. Ela garante a robustez do software, avisando ao eletricista que o valor inserido é fisicamente impossível ou inválido para o cálculo.

O programa utiliza while True para criar um loop infinito, permitindo que o eletricista realize diversos cálculos em sequência, saindo apenas quando escolher a opção '4'.

4. Suponha que o professor Atila possua dois logins na rede do SENAI-SP. 
Construa um programa que valide o acesso do professor à rede. 
Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”.
Caso contrário, “Usuário e senha não conferem”.
Dados dos dois logins:
login 1			login 2
usuário: atila		usuário: olivi
senha: 12345		senha: 54321
Salvar o código como: dois_logins.py

Sistema de Validação de Acesso - Rede SENAI-SP

Definição dos dados de login válidos (Dados do exercício)

#Login 1: atila / 12345

#Login 2: olivi / 54321

user1, pass1 = "atila", "12345"
user2, pass2 = "olivi", "54321"

Entrada de dados

O programa solicita que o usuário insira seu login e senha

print("--- Login SENAI-SP ---")
usuario_input = input("Usuário: ")
senha_input = input("Senha: ")

Estrutura de Decisão (Validação)

Verifica se o par informado corresponde a algum dos logins cadastrados.

O operador 'or' permite a validação dos dois pares de usuários distintos.

if (usuario_input == user1 and senha_input == pass1) or \
   (usuario_input == user2 and senha_input == pass2):
   
    # Se uma das condições for verdadeira, o acesso é garantido
    
    print("Seja bem vindo!")
    
else:

    # Se nenhuma for verdadeira, o acesso é negado
    
    print("Usuário e senha não conferem")

Justificativa das Estruturas de Decisão

Uso do if / else: Essencial para controle de fluxo. O programa precisa decidir entre dois caminhos exclusivos (sucesso ou erro) baseando-se na entrada do usuário.

Operador lógico and: Utilizado dentro dos parênteses (usuario == ... and senha == ...) para garantir que ambos, usuário e senha, estejam corretos para aquele login específico.

Operador lógico or: Utilizado para conectar as duas validações. Ele permite que o programa aceite o par 1 OU o par 2, flexibilizando o acesso para mais de uma credencial válida.

5. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

Código	Condição de Pagamento	Desconto (%)
1 	À vista (em espécie) 	10
2	Cartão de débito	5
3	Cartão de crédito	3
4	PIX			7.5

Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
Ao fim, o programa deve informar o valor final a ser pago.
Salvar o código como: black_friday.py

Programa para cálculo de desconto - Black Friday

Solicita o preço total da venda

preco_total = float(input("Digite o valor total da venda (R$): "))

Exibe as opções de pagamento para o operador

print("\nCÓDIGO | CONDIÇÃO DE PAGAMENTO | DESCONTO")
print("1      | À vista (espécie)     | 10%")
print("2      | Cartão de débito      | 5%")
print("3      | Cartão de crédito     | 3%")
print("4      | PIX                   | 7.5%")

Solicita o código da forma de pagamento

codigo = int(input("\nDigite o código da forma de pagamento: "))

Estrutura de decisão para definir o percentual de desconto

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

Cálculo do valor final

A fórmula aplicada é: Valor * (1 - Porcentagem/100)

valor_final = preco_total * (1 - desconto / 100)

Exibe o resultado final formatado com duas casas decimais

print(f"\nDesconto aplicado: {desconto}%")
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")

Justificativa das Estruturas Utilizadas

float() e int(): Essenciais para garantir que os dados vindos do teclado (que por padrão são textos/strings) possam ser usados em cálculos matemáticos.

if: Utilizado para testar a primeira condição (Código 1).

elif (else if): Utilizado para testar as condições subsequentes. O uso do elif é mais eficiente que vários if isolados, pois assim que o Python encontra uma condição verdadeira, ele ignora as demais, economizando processamento.

else: Funciona como uma "saída de segurança" para tratar erros de digitação (caso o operador digite um código que não existe na tabela).

F-strings (f"..."): Utilizadas na saída de dados para facilitar a inserção de variáveis dentro do texto e formatar o valor monetário com duas casas decimais (:.2f).

6. Desenvolva um programa que receba uma string e exiba a mesma na tela. Se o valor digitado for em branco exibir 'Dado inválido'
Salvar o código como: validar_str.py

Programa para validação de string em branco

def main():

    # Entrada de dados
    
    # A função input() recebe o texto do usuário.
    
    # Usamos strip() para remover espaços em branco desnecessários no início/fim.
    
    entrada = input("Digite algo: ").strip()

    # Estrutura de Decisão (if/else)
    
    # Justificativa: Necessária para verificar se a string está vazia após o strip().
    
    # if not entrada: verifica se a string é falsa (vazia "" ou apenas espaços)
    
    if not entrada:
    
        # Se for vazio, exibe a mensagem de erro
        
        print("Dado inválido")
        
    else:
    
        # Se contiver conteúdo, exibe o valor digitado
        
        print(f"Você digitou: {entrada}")

Executa o programa

if __name__ == "__main__":
    main()

Justificativa e Explicação das Estruturas de Decisão

No código acima, a estrutura de decisão principal é o bloco if / else.

Por que usar if not entrada?
Finalidade: Em Python, uma string vazia "" é considerada "falsy" (falsa em um contexto booleano). A estrutura if not é a maneira mais concisa de verificar se a variável entrada está vazia após a remoção de espaços em branco (feita pelo .strip()).
Comportamento: Se o usuário pressionar Enter sem digitar nada, ou digitar apenas espaços, entrada será "", fazendo com que if not "" seja True, resultando na exibição de "Dado inválido".

Por que usar else?
Finalidade: O else garante que o bloco de código de sucesso só será executado se a condição do if for falsa. Ou seja, quando a string não estiver vazia, ele exibe o conteúdo digitado.

Uso do .strip() (Importante): Essa função é usada para remover espaços em branco apenas no início e no fim da string. Isso garante que entradas como " " (apenas espaços) também sejam consideradas "Dada inválido", aumentando a robustez do programa.
