# Aula 01: técnicas de programação IMPACTA 8 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Revisão: Estruturas de controle

# %% --begin
"""
A sequencialidade é a forma padrão de execução em Python

As instruções são executadas linha a linha, de cima para baixo, na ordem em que aparecem no código, a menos que haja instruções de controle de fluxo que modifiquem esse comportamento
Estrutura Sequencial

<instrução>
<instrução>
<instrução>
"""
# Exemplo: Estrutura sequencial

a = int(input())
b = int(input())

soma = a + b

print(soma)

# %% Estrutura de seleção simples
"""
Utiliza-se o if, seguido da expressão a qual se deseja avaliar e, em um nível
de indentação à direita, o bloco de instruções a ser executado caso a
condição seja verdadeira.

if <expressão>:

<instrução 1>

<instrução 2>
"""
# Exemplo: Estrutura de seleção simples
idade = int(input())

if idade<18:

    print("menor de idade")

# %% Estrutura de seleção composta
"""
No mesmo nível de indentação do if, utiliza-se o else para criar o caminho
que leva ao bloco de instruções a ser realizado caso a expressão lógica
resulte em falso. O bloco de instruções do else deve estar no mesmo nível
de indentação do bloco do if.

    
if <expressão>:

    <instrução 1>

    <instrução 2>

else:

    <instrução 1>
"""

# Exemplo: Estrutura de seleção composta
idade = int(input())

if idade<18:

    print("menor de idade")

else:

    print("maior de idade")

# %% Estrutura de seleção aninhada
"""
Utiliza-se if e else em diferentes níveis de indentação.

if <condição 1>:
    if <condição 2>:
        if <condição 3>:
            <instrução 1>
        else:
            <instrução 2>
    else:
        <instrução 3>
else:
    if <condição 4>:
        <instrução 4>
    else:
    <instrução 5>
"""

# %% Estrutura de seleção encadeada
"""
O aninhamento ocorre no caminho do falso para cada elemento de decisão 
Podemos combinar o else com if, formando um elif:

if <condição 1>:
    <instrução 1>
elif <condição 2>:
    <instrução 2>
elif <condição 3>:
    <instrução 3>
elif <condição 4>:
    <instrução 4>
else:
    <instrução 1>
    
"""
# %% Exemplo: Estrutura de seleção encadeada
idade = int(input())

if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")
    
# %% Estrutura de repetição indefinida
"""
while <condição>:
    <bloco de instruções>
"""
# %% Estrutura de repetição definida
""" 
Utilizando for:

for i in range (5):
    <bloco de instruções>
    
Utilizando while:

i = 0
while i<5:
    <bloco de instruções> 
"""

# %% --end