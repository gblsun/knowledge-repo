# Aula 02: técnicas de programação IMPACTA 9 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Revisão: Funções Estruturas de dados sequenciais

"""
Revisão sobre funções, escopo, passagem de parâmetro por valor e por referência, estruturas de dados sequenciais e sequências aninhadas

Funções:

-Sequência de instruções que executa alguma tarefa específica e que tem um nome
-Objetivo bem claro
-Redução do tamanho do código
-Divisão do código - Paralelismo na construção
-Reutilização código - Redução do tempo de construção e testes

Parâmetros de funções:

-Parâmetros: dados que fornecemos a função paraela cumprir seu objetivo
-As funções podem ter qualquer número de parâmetros
-As funções podem não ter parâmetros

Retorno de funções:

-O retorno de uma função é o valor que ela devolve para quem a invocou.
-O retorno é a saída da função.
-Usamos retorno quando queremos usar o cálculo da função (não só exibir).

Funções em Python:


Sequência de instruções que executa alguma tarefa específica e que tem um nome.

Integradas: na própria linguagem de programação e disponíveis para uso a qualquer momento
Importadas: criadas por outros programadores e disponibilizadas para serem incluídas no ambiente de programação/
Definidas: construídas pelo próprio programador no código-fonte

Importação de módulos

Usamos o comando import para carregar módulos extras do Python
"""
# %% Importação de módulos
import math
import time

print(math.pi)
time.sleep(3)
print(math.log(10))


""" 
Para definir uma função, usamos a palavra chave def

def <nome da função>([<parâmetros>]):
    <bloco de código da função>
"""
# %% Exemplo:
def somar(n1, n2):
    soma = n1 + n2
    return soma
print
# %% --end
