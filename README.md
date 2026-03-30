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

