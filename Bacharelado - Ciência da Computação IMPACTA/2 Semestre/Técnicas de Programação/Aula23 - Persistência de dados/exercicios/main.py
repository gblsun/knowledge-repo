# imports
import json
import
# funções
def criar_perfis():
    dados = {}

    while True:
        nome = input("Digite o seu nome: ")
        senha = input("Digite o sua senha: ")
        dados[nome] = senha

        continuar = input("Deseja continuar outro perfil? (sim/não)").strip().lower()
        if continuar != "sim":
            break

    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)

    print("Perfis e senhas criadas com sucesso!")
# def alterar_senha():
    
# def listar():
    
# programa principal

print("Seja bem-vindo(a) ao algoritmo genérico de login!")
print("Criado por Gabriel Muchon Pavanelli ;)")
criar_perfis()