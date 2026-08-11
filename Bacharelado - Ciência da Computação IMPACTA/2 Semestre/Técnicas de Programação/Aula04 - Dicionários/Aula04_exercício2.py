# Aula: técnicas de programação IMPACTA 16 e 17 de Agosta de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Novas estruturas de Dados:
# Dicionários

# Exercício II
# Escreva uma função que conta a quantidade devogais em um texto e armazena tal quantidade emum dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogalaparece no texto. A função deve receber o texto como entrada e retornar o dicionário. Por exemplo, para o texto abaixo: texto = 'faculdade impacta de tecnologia' A função deve devolver o seguinte dicionário:{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }

# ainda não terminado
# %% ---begin
# O trecho de código `contagem = {}`, `texto = input (" digite seu texto: ")` e `vogais =" aeiou "` é
# Inicializando um dicionário chamado `contagem`, levando o usuário a inserir uma sequência de texto e definir
# Uma variável de string `vogais` contendo as vogais" aeiou ", respectivamente.
contagem = {}
texto = input("Digite seu texto: ")
vogais = "aeiou"

# As linhas que você forneceu estão contando as ocorrências de cada vogal ('a', 'e', ​​'i', 'o', 'u') no
# texto de entrada.Vamos quebrar uma das linhas como exemplo:
contagem_a = sum(1 for char in texto.lower() if char in "a")
contagem_e = sum(1 for char in texto.lower() if char in "e")
contagem_i = sum(1 for char in texto.lower() if char in "i")
contagem_o = sum(1 for char in texto.lower() if char in "o")
contagem_u = sum(1 for char in texto.lower() if char in "u")

# The lines `contagem["a"] = contagem_a`, `contagem["e"] = contagem_e`, `contagem["i"] = contagem_i`,
# `contagem["o"] = contagem_o`, and `contagem["u"] = contagem_u` are assigning the counts of each
# vowel ('a', 'e', 'i', 'o', 'u') in the input text to the corresponding keys in the dictionary
# `contagem`.
contagem["a"] = contagem_a
contagem["e"] = contagem_e
contagem["i"] = contagem_i
contagem["o"] = contagem_o
contagem["u"] = contagem_u

# A instrução `print (contagem)` está emitindo o dicionário `contagem` para o console.Isso vai
# Exiba os pares de valor-chave no dicionário, mostrando a contagem de cada vogal ('a', 'e', ​​'i', 'o',
# 'u') no texto de entrada que foi fornecido pelo usuário.
print(contagem)
# %% ---end
