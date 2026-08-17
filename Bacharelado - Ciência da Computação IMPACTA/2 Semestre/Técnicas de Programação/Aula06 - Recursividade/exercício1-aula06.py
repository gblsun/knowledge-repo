# Aula 6: técnicas de programação IMPACTA 23 de Agosto de 2024

# Os números de Fibonacci constituem uma sequência de números na qual os dois primeiroselementos são 0 e 1 e os demais, a soma dos dois elementos imediatamente anteriores.
# A sequência formada pelos 10 primeiros números de Fibonacci é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 definição matemática para encontrar o N-ésimo número na sequência de Fibonacci também usa recursão

# Crie uma função fib(n) que retorna o n-ésimo número da sequência de Fibonacci.
# %% --begin

def fib(n):
    """
    A função calcula o número de fibonacci recursivamente em Python.
    
    : param n: no trecho de código fornecido, a função `fib (n)` calcula o número de fibonacci do Fibonacci
    recursivamente.A função retorna o número de Fibonacci na posição `n`
    : Return: o código está calculando o 10º número na sequência de Fibonacci usando um recursivo
    função.A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma do
    dois números anteriores.
    """
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fib(n-1)+ fib(n-2))

print(fib(10))
# %% --end
