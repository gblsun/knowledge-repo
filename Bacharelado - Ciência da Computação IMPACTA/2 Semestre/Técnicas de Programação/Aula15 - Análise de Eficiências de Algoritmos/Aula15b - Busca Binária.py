'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 15: técnicas de programação IMPACTA 27 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳

Busca binária

1. A função recebe um valor que deve ser buscado na sequência;
2. inicio: índice do primeiro item da sequência;
3. fim: o índice do último item da sequência;
4. intervalo de busca: intervalo [inicio..fim]
5. Valor buscado é comparado com o item que está no índice do meio do intervalo de busca: (inicio+fim)//2
6. Caso sejam iguais, a função é encerrada com o retorno do índice deste item;
7. Caso não sejam iguais, o valor está em [inicio..meio-1] ou em [meio+1..fim]
8. Caso o valor buscado seja menor que o item do meio, o procuraremos dentre
os menores, atualizando o intervalo de busca para [inicio..meio-1];
9. Caso o valor buscado seja maior que o item do meio, o procuraremos dentre os maiores, atualizando o intervalo de busca para [meio+1..fim];
10. O procedimento continuará voltando ao passo 5 enquanto o valor buscado não for encontrado e o intervalo de busca [inicio..fim] não for vazio
11. Se [inicio..fim] ficou vazio, isto é, inicio > fim, o valor não foi encontrado e será retornado um valor indicativo, neste caso, None
'''