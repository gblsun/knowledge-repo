"""
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 13: técnicas de programação IMPACTA 05 de Setembro de 2024                |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercícios 2:                                                              |
|        Tratamento de excessões                                                |
<-------------->x<-------------->x<------------->x<------------->x<------------->

II. Sabemos que o algoritmo de busca binária só se aplica a sequências ordenadas. Crie uma função chamada busca_binaria. Esta função deve,inicialmente, verificar se a sequência está ordenada. Se não estiver, faça com que uma exceção personalizada UnsortedSequenceError seja lançada, com a mensagem “A sequência não está ordenada”. Se a sequência estiver ordenada, a função deve realizar a busca binária, retornando True caso o valor seja encontrado e False caso contrário. Utilize o programa principal abaixo para testar.

sequencia1 = [10,20,30,40,50]
sequencia2 = [20,30,10,50,40]

print(busca_binaria(sequencia1,30)) #True
print(busca_binaria(sequencia2,30)) #UnsortedSequenceError: A sequência não está ordenada"""