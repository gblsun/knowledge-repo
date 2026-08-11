# Jogo da Forca
# Projeto/exercício feito para disciplina de Técnicas de Programação
# %%

# //Importações
import requests

# importa a biblioteca requests
# é usado para fazer requisições HTTP.
import random

# importa a biblioteca random
# é usado para gerar valores aleatórios

# //Definição da URL e Requisição
url = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
# Define URL do arquivo de dicionário PT-BR

response = requests.get(url)
# requisição HTTP GET para o URL definido para obtenção do conteúdo

response.raise_for_status()
# verificação se a requisição foi bem-sucedida
#   Status
#       404 - Not found
#       500 - Internal Server Error
#       200 - OK

print(response.status_code)

# //Processamento da Resposta
palavras = response.text.splitlines()
# response.text: obtenção do conteúdo da resposta como STRING
# splitlines(): Serve para dividir todo o conteúdo em uma lista de linhas,
#   ou seja, cada linha é uma palavra
#       - palavras - é onde são alocadas todas as palavras do arquivo;

palavras = [p for p in palavras if len(p) > 2]
# p for p in palavras
#   para cada palavra em 'palavras', a variável 'p' assume o valor da palavra atual
# if len(p) > 2
#   Verificação do comprimento da palavra. Maior que 2?

palavra_aleatoria = random.choice(palavras)
# Escolhe uma palavra aleatória do arquivo 'palavras' e aloca na variável palavra_aleatoria

# //Começo do Jogo
print()
print(
    "Bem-vindo ao jogo da forca!\nO jogo consiste em tentar descobrir a palavra que é gerada aleatoriamente.\nIsto em apenas 6 chances!! \nVocê consegue??\n"
)

numero_letras = len(palavra_aleatoria)
# número de letras - obtenção do número de letras na palavra aleatória
letras_descobertas = ["_" for _ in range(numero_letras)]
# criação de uma lista com o mesmo número de letras.
#   Isso para representação das letras que ainda não foram adivinhadas;
#       Ocultas, por assim dizer.

erros = 0
# Inicialização do contador de erros igual a zero

# // ASCII Art
#   ref: https://ascii-art.botecodigital.dev.br/
arte_ascii = [
    """
                                          
  ..                                                  
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
      ##                                          
    ########                                      
                                                                                  
    """,
    """
                                                            
                                                            
                                                      
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                            ##            
      ##                            ##            
      ##                            ##            
      ##                            ##            
      ##                            ##            
      ##                            ##            
      ##                            ##            
      ##                                          
      ##                                          
      ##                                          
      ##                                          
    ########                                      
                                                                                                
    """,
    """
                                                            
                                                            
                                                      
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                            ##            
      ##                          ++##            
      ##                        mm####            
      ##                      MM##  ##            
      ##                      ##    ##            
      ##                            ##            
      ##                            ##            
      ##                                          
      ##                                          
      ##                                          
      ##                                          
    ########                                      
                                                                                                
    """,
    """
                                                            
                                                            
                                                      
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                            ##            
      ##                          ++##            
      ##                        mm####            
      ##                      MM##  ##            
      ##                      ##    ##            
      ##                            ##            
      ##                          ####            
      ##                        ####              
      ##                      ####                
      ##                      ##                  
      ##                                          
    ########                                      
                                                                                                
    """,
    """
                                                            
                                                            
                                                      
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                            ##            
      ##                          ++##            
      ##                        mm####            
      ##                      MM##  ##            
      ##                      ##    ##            
      ##                            ##            
      ##                          ######          
      ##                        ####  ####        
      ##                      ####      ####      
      ##                      ##          ##      
      ##                                          
    ########                                      
                                                                                                
    """,
    """
                                          
  ..                                                  
    ####################################--        
      ##    ####                    ##            
      ##  ####                      ##            
      ######                        ##            
      ####                        ######          
      ##                        ##                
      ##                        ##      ##        
      ##                        ##      ##        
      ##                          ######          
      ##                            ##            
      ##                          ++####          
      ##                        mm########        
      ##                      MM##  ##  ####      
      ##                      ##    ##    ##      
      ##                            ##            
      ##                          ######          
      ##                        ####  ####        
      ##                      ####      ####      
      ##                      ##          ##      
      ##                                          
    ########                                      
                                                                                  
    """,
]

# //Loop do Jogo
while erros < 6 and "_" in letras_descobertas:
    # Enquanto o usuário não errar 6 e houver letras ocultas:

    tentativa = input("Digite uma letra ou a palavra completa: ").strip().lower()
    # Solicita ao usuário uma tentativa
    #   .strip = remove os espaços
    #   .lower = converte todos os caracteres da string para minúsculas.

    # //Verificação da tentativa
    if len(tentativa) > 1 and not tentativa.isalpha():
        # Verifica se a entrada do usuário é válida (só uma letra ou uma palavra)
        print("Entrada inválida. Digite apenas uma letra ou uma palavra.")
        continue

    if tentativa == palavra_aleatoria:
        # se a tentativa for igual à palavra_aleatoria inteira:
        letras_descobertas = list(palavra_aleatoria)
        # Substitui a lista letras_descobertas pela palavra correta
        break

    elif tentativa in palavra_aleatoria:
        # se a tentativa está dentro da palavra aleatória:
        if len(tentativa) == 1:
            # é só uma letra?
            letra = tentativa
            # armazena a tentativa na variável
            print(f"Parabéns! A letra '{letra}' inserida contém na palavra:")
            # exibe a mensagem indicando onde está a letra;

            for i, l in enumerate(palavra_aleatoria):
                # Itera sobre cada letra da 'palavra_aleatoria'
                #   fornece o índice dessa letra;
                #       enumerate: gera pares entre índice (i) e letra (l) para o posicionamento na string 'palavra_aleatoria'.
                if l == letra:
                    # verifica se a letra atual (l) é igual à letra que o usuário colocou (letra);
                    letras_descobertas[i] = letra
                    # atualiza a lista 'letras_descobertas' com a letra correta na posição correspondente ao índice (i);

        else:
            print(f"A palavra '{tentativa}' não é a palavra correta.")

    else:
        erros += 1
        print(f"A letra '{tentativa}' não está na palavra. Erros: {erros}/6")
        print(f"Você tem {6 - erros} chances restantes.")
        if erros <= len(arte_ascii):
            print(arte_ascii[erros - 1])
            # exibe a arte número (erros - 1)

    print(" ".join(letras_descobertas))

if "_" not in letras_descobertas:
    print("Parabéns! Você descobriu a palavra!")
    #
else:
    print("Você perdeu!")
    print(f"A palavra era: {palavra_aleatoria}")

# %%
