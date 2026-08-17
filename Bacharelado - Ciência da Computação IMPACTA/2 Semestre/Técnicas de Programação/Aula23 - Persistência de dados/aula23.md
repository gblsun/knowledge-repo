<!-- 
Aula 19: técnicas de programação IMPACTA 11 de Outubro de 2024
Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  
 -->
# Persistência de dados

## Histórico
* Antes da introdução dos sistemas gerenciadores de bancos de dados (SGBDs), os programas de computadores já tinham a finalidade de acessar e manipular dados
* Os dados ficavam armazenados em arquivos
* Os programas precisavam conhecer a estrutura de armazenamento dos dados nos arquivos
* SGBDs surgiram como sistemas intermediários entre os programas e os arquivos de dados 
* Ainda existem situações em que é preferível realizar o acesso direto aos dados

## Armazenamento de dados em arquivos 
(quando utilizar armazenamento em arquivos)

* Arquivo: área de memória (não volátil) onde podemos realizar a leitura e a escrita de dados
* Para que programa possa interagir com os arquivos, é necessário:
* * Saber o local onde o arquivo está (caminho)
* * Conhecer a estrutura para que o arquivo possa ser consultado (leitura)
* * Definir o nome e o local onde será guardado ou alterado (escrita).

## Caminho dos arquivos
* Caminho absoluto: começa a partir da unidade básica do sistema (C no Windows, home no Linux)
* Caminho relativo: começa a partir da localização do diretório atual