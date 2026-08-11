'''
Apenas uma revisão para maior compreensão do exercício.
09/10
→ 
↳
'''


# Identificação e diferenciação abordagem responsiva e iterativa

'''
→ Abordagem Recursiva
I. Definição: A recursão ocorre quando uma função se chama diretamente ou indiretamente. Um problema é resolvido quebrando-o em subproblemas menores até chegar a um caso base, onde a solução é simples.

II. Estrutura: Uma função recursiva geralmente tem duas partes principais:

    ↳ Caso base: Define quando a recursão para (condição de término).
    ↳ Passo recursivo: Quando a função se chama novamente com um problema menor.
    
III: Exemplo Recursivo (Fatorial):'''    

def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Passo recursivo
'''
IV. Vantagens:

    ↳ Mais intuitiva para problemas que possuem uma natureza recursiva, como árvores, grafos, e certos problemas de divisão e conquista (ex.: busca binária).
    ↳ O código tende a ser mais conciso e fácil de entender.

V. Desvantagens:

    ↳ Pode consumir muita memória, especialmente com entradas grandes, pois cada chamada recursiva é colocada na pilha de chamadas.
    ↳ Pode ser menos eficiente em termos de tempo e espaço, dependendo da profundidade da recursão.


Abordagem Iterativa:

I. Definição: Iteração utiliza estruturas como loops (for, while) para repetir um bloco de código até que uma condição seja satisfeita.

II. Estrutura: Uma função iterativa resolve o problema repetindo uma operação até atingir o resultado desejado, sem o uso de chamadas adicionais a si mesma.

III. Exemplo Iterativo (Fatorial):'''

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

'''
IV. Vantagens:

    ↳ Uso eficiente de memória: Não envolve a criação de novas pilhas de chamadas, tornando-a mais eficiente em termos de uso de memória.
    ↳ Melhor performance: Para entradas grandes, a iteração costuma ser mais rápida do que a recursão, devido à ausência de overhead de chamadas de função.

V. Desvantagens:

    ↳ Pode ser menos intuitiva para certos problemas naturalmente recursivos.
    ↳ O código pode ser mais longo e complexo em alguns casos, principalmente em problemas como árvores ou grafos.
'''

