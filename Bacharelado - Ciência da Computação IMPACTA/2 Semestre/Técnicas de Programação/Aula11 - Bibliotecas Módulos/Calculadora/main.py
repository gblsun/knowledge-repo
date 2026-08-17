# %%
# imports
import padrao
import cientifica
import trigonometrica
import os

# Programa Principal
while True:
    os.system("cls")
    print("Seja bem vindo à calculadora!\n")
    print("Qual calculadora deseja utilizar?")
    print("Digite 1 - Calculadora Padrão")
    print("Digite 2 - Calculadora Cientifica")
    print("Digite 3 - Calculadora Trigonométrica")
    print("Digite 4 - Sair")  # Opção para sair
    escolha = int(input("\nDigite sua escolha: "))

    if escolha == 1:
        os.system("cls")
        while True:  # Loop para operações na calculadora padrão
            print("Qual Operação básica deseja fazer?")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Voltar")  # Opção para voltar ao menu anterior
            escolha_operacao = int(input("\nDigite sua escolha: \n\n"))

            if escolha_operacao == 1:
                os.system("cls")
                a = int(input("Digite o primeiro valor para somar: "))
                b = int(input("Digite o segundo valor para somar: "))
                print(f"O resultado de {a} + {b} é igual a {padrao.soma(a, b)}\n")

            elif escolha_operacao == 2:
                os.system("cls")
                a = int(input("Digite o primeiro valor para subtrair : "))
                b = int(input("Digite o segundo valor para subtrair: "))
                print(f"O resultado de {a} - {b} é igual a {padrao.subtracao(a, b)}\n")

            elif escolha_operacao == 3:
                os.system("cls")
                a = int(input("Digite o primeiro valor para multiplicar: "))
                b = int(input("Digite o segundo valor para multiplicaro: "))
                print(f"O resultado de {a} × {b} é igual a {padrao.multiplicacao(a, b)}\n")

            elif escolha_operacao == 4:
                os.system("cls")
                a = int(input("Digite o primeiro valor para dividir: "))
                b = int(input("Digite o segundo valor para dividir: "))
                print(f"O resultado de {a} ÷ {b} é igual a {padrao.divisao(a, b)}\n")

            elif escolha_operacao == 5:
                os.system("cls")
                break  # Sai do loop de operações para voltar ao menu principal
            else:
                print("Operação inválida!")

    elif escolha == 2:
        while True:
            print("Qual Operação deseja fazer?")
            print("1 - exponenciação")
            print("2 - Logaritmo")
            print("3 - Voltar")  # Opção para voltar ao menu anterior
            escolha_operacao = int(input("\nDigite sua escolha: "))

            if escolha_operacao == 1:
                os.system("cls")
                a = int(input("Digite o primeiro valor para a exponenciação: "))
                b = int(input("Digite o segundo valor para a exponenciação: "))
                print(f"O resultado de {a} ^ {b} é igual a {cientifica.exponenciacao(a, b)}\n")
            elif escolha_operacao == 2:
                os.system("cls")
                a = int(input("Digite o valor para o logaritmo: "))
                print(f"O resultado de log({a}) é igual a {cientifica.logaritmo(a)}\n")

            elif escolha_operacao == 3:
                os.system("cls")
                break
            
    elif escolha ==3:
        while True:
            print("Qual Operação deseja fazer?")
            print("1 - Seno")
            print("2 - Cosseno")
            print("3 - Tangente")
            print("4 - Voltar")  # Opção para voltar ao menu anterior
            escolha_operacao = int(input("\nDigite sua escolha: "))
            
            if escolha_operacao == 1: 
                os.system("cls")
                a = int(input("Digite o valor para calcular o Seno: "))
                print(f"O resultado de sen({a}) é igual a {trigonometrica.seno(a)}\n")
                
            elif escolha_operacao == 2: 
                os.system("cls")
                a = int(input("Digite o valor para calcular o Cosseno: "))
                print(f"O resultado de cos({a}) é igual a {trigonometrica.cosseno(a)}\n")
                
            elif escolha_operacao == 3: 
                os.system("cls")
                a = int(input("Digite o valor para calcular o tangente: "))
                print(f"O resultado de tg({a}) é igual a {trigonometrica.tangente(a)}\n")
                
            elif escolha_operacao == 4:
                os.system("cls")
                break
                
    elif escolha == 4:
        print("Saindo...")
        break  # Sai do loop principal e encerra o programa

    else:
        print("teste")
# %%
