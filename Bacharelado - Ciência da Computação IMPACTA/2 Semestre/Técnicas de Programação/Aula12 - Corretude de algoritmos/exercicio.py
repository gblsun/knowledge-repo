'''
Considere a seguinte função, que retorna a soma dos quadrados dos n primeiros números naturais: Avalie a corretude desta função empiricamente e formalmente.

def soma_quadrados(n): 
    return n * (n + 1) * (2 * n + 1) / 6

Obs: a soma dos quadrados dos n primeiros números naturais é dada por: 
    Sn = 1² + 2² + 3² + ... n²
'''

def soma_quadrados(n): 
    return n * (n + 1) * (2 * n + 1) / 6

print(soma_quadrados(1))
print(soma_quadrados(2))
print(soma_quadrados(3))
