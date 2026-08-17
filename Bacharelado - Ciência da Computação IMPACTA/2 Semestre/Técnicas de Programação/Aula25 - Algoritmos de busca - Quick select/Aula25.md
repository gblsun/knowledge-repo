# **Quick select**

##### Aula dada: 01/11/2024. 
##### Técnicas de Programação. Prof: Vitor Fulan.
##### Anotações feitas por Gabriel Muchon Pavanelli GitHub: gblsun

## **Busca em sequências**

* Permitem verificar se um item pertence a um vetor
* Possibilitam acessar dados associados ao item buscado
* Algoritmos de busca
* * Busca binária
* * Busca linear

## **Quick select**

1. Escolher um pivô
2. Particionar o vetor em dois:
3. Elementos menores ou iguais ao pivô ficam à sua esquerda (subvetor esquerdo)
4. Elementos maiores que o pivô ficam à sua direita (subvetor direito)
5. Retornar o índice do pivô ao final do particionamento
6. Se o índice do pivô após a partição for igual a k, então o pivô é o k-ésimo menor elemento do vetor, e o algoritmo retorna esse valor
7. Se o índice do pivô for maior que k, então o k-ésimo menor elemento está à esquerda do pivô. Aplicar quick select no subvetor esquerdo
8. Se o índice do pivô for menor que k, então o k-ésimo menor elemento está à direita do pivô. Aplicar quick select no subvetor direito
