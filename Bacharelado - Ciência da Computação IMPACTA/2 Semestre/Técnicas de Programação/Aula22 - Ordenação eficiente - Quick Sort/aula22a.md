# **Quick sort**
## Estratégia “dividir para conquistar”
* O funcionamento do Quick Sort baseia-se em uma rotina fundamental cujo nome é particionamento
* O particionamento escolhe um item qualquer do vetor (chamado de pivô) e o coloca em uma posição tal que todos os elementos à esquerda são menores ou iguais, e todos os elementos à direita são maiores

## Escolha do pivô

* Quando o particionamento divide a lista em partes mais ou menos do mesmo tamanho, o algoritmo é mais eficiente.
* Porém se a partição for muito desigual, o algoritmo é menos ineficiente.
* Para diminuirmos a chance de ocorrência do pior caso, escolhemos como pivô o elemento de uma posição aleatória (pode ser difícil de verificar na prática)
* A ocorrência do melhor e pior caso é bem rara:
* * Pior Caso: é causado por sucessivas péssimas escolhas de pivô, que sempre divide a lista em duas porções de tamanho 0 e n-1.
* * Melhor Caso: quando o pivô sempre ficar no meio da lista, dividindo-a em duas porções iguais.
* Há experimentos que demonstram que o Quick Sort, em seu melhor caso, é por volta de 3x mais eficiente que o Merge Sort
* Porém, o tempo de execução do Merge Sort é constante para qualquer caso
Considera-se que os dois métodos possuem tempo de execução similar
