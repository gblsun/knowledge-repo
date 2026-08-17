'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 23: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

continuando...

Leitura dos arquivos

→ Função integrada open
→ Diferentes formas de abrir um arquivo

Caractere | Significado
'r'       |abre para leitura (padrão)
'w'       |abre para escrita truncando o arquivo primeiro caso ele exista
'x'       |abre para criação exclusiva falhando caso o arquivo exista
'a'       |abre para escrita anexando ao final do arquivo caso ele exista
'b'       |modo binário
't'       |modo texto (padrão)
'+'       |abre para atualização (leitura e escrita)
'''
# %%
f = open('teste.txt', 'w')
f.write('Ola Mundo!\n')
f.close()

'''
→ Gerenciamento de contexto: palavra chave with permite abrir o arquivo, executar o que é necessário e garante que o arquivo será fechado ao final das instruções'''
# %%

with open('teste2.txt', 'w’) as f:
    f.write('Olá novamente!\n')

'''
→ Ao abrirmos um arquivo de texto em Python, nos é retornado um objeto que é uma instância da classe TextIOWrapper, que faz parte do módulo io.
→ Pode-se então utilizar métodos desta classe para manipular o arquivo read e readlines: lê todo o conteúdo, retornando str ou list[str]'''
# %%
with open('teste.txt', 'r') as f:
    texto = f.read()

'''
→ readline: lê o conteúdo do arquivo a partir da posição do marcador até encontrar uma quebra de linha'''
with open('teste.txt', 'r') as f:
    texto = f.readline()
'''
→ tell e seek: Lê e modifica a posição do marcador'''
# %%
with open('teste.txt', 'r') as f:
    print(f.tell()) # exibe a posição atual
    f.seek(5) # move a posição atual para o índice 5
'''
→ write e writelines: escreve o conteúdo de uma str ou sequência de str no arquivo'''
# %%
texto = 'escrevendo a primeira frase'
    with open('teste.txt', 'w') as f:
        f.write(texto)
'''
→ readline: lê o conteúdo do arquivo a partir da posição do marcador até encontrar uma quebra de linha'''
# %%
with open('teste.txt', 'r') as f:
    texto = f.read()
'''
→ tell e seek: Lê e modifica a posição do marcador'''
# %%
with open('teste.txt', 'r') as f:
    print(f.tell()) # exibe a posição atual
    f.seek(5) # move a posição atual para o índice 5

'''
→ Arquivos CSV (Comma-Separated Values): tipo de arquivo de texto que armazena dados tabulares
    ↳ Cada linha do arquivo representa uma linha na tabela de dados
    ↳ As colunas são separadas por um caractere delimitador, comumente uma vírgula (,), ponto e vírgula (;) ou tabulação (\t).
→ O Python disponibiliza o módulo csv para manipulação destes arquivos'''
# %%
import csv

with open('estoque.csv', 'w', newline='',encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(estoque)

'''
→ Além do módulo csv, a biblioteca pandas oferece funcionalidades abrangentes para ler, escrever, manipular e analisar dados tabulares, incluindo suporte nativo para o formato CSV.
→ Os dados tabulares são armazenados em um tipo de dados chamado DataFrame'''
# %%
import pandas as pd

dados = pd.read_csv('arquivo.csv')

'''
→ Pandas oferece uma vantagem significativa em relação ao módulo csv devido à sua amplitude de funcionalidades, facilidade de uso e eficiência
→ Amplamente utilizado em aplicações de análise e ciência de dados

→ Funcionalidades do pandas
    ↳ Leitura e escrita de dados: métodos para ler e escrever dados em uma variedade de formatos, incluindo CSV, Excel, SQL, etc.
    ↳ Indexação e seleção: permite selecionar e manipular dados com facilidade usando indexação baseada em rótulos ou posições
    ↳ Limpeza e transformação de dados: permite limpar e transformar dados, incluindo remoção e preenchimento de valores faltantes, renomeação de colunas, e aplicação de funções de mapeamento.
    ↳ Agregação e agrupamento: oferece operações de agregação e agrupamento em conjuntos de dados
    ↳ Operações de junção e concatenação: permite realizar operações de junção e mesclagem entre diferentes conjuntos de dados
    ↳ Outras funcionalidades: visualização de dados, manipulação de Datas e Horas, análise estatística, etc.

Arquivos json

→ JSON (JavaScript Object Notation): formato de dados leve e legível por humanos que é comumente usado para armazenar e trocar dados estruturados.
→ Baseados em um subconjunto da linguagem JavaScript, mas são independentes de linguagem de programação
→ Um arquivo JSON consiste em pares chave-valor, onde os valores podem ser strings, números, booleanos, arrays, objetos ou valores nulos
→ Estrutura útil para representar dados hierárquicos e complexos, como configurações de aplicativos, dados de API da web, entre outros. 
→ Em Python: módulo json para manipulação deste tipo de arquivo

| Python                | JSON     |
|-----------------------|----------|
| dict                  | object   |
| list, tuple           | array    |
| str                   | string   |
| int, float e Enums    | number   |
| True                  | true     |
| False                 | false    |
| None                  | null     |

→ Em Python: módulo json para manipulação deste tipo de arquivo
    ↳ Codificação (serialização) de um objeto em Python para JSON: json.dump (serializar o objeto e gravar em um arquivo JSON) e json.dumps (serializar um objeto e retorná-lo como str)
    ↳ Decodificação (desserialização) de um JSON para um objeto em Python:
    ↳ json.load (desserializar o arquivo JSON e retornar objeto Python) e
    ↳ json.loads(desserializar uma str correspondente ao JSON e retornar um objeto Python)
    
Codificação:'''
# %%
import json

dados = {"nome": "Alice", "idade": 30}

json_string = json.dumps(dados)
print(json_string)

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)

# %% 
# Decodificação

import json

json_string = '{"nome": "Alice", "idade": 30}'

dados_str = json.loads(json_string)
print(dados_str)

with open('dados.json', 'r') as arquivo:
    dados_arquivo = json.load(arquivo)

print(dados_arquivo)
