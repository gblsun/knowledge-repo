'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 11: técnicas de programação IMPACTA 12 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Bibliotecas 
    em
        Python 

(continuação):


Scripts

→ Em Linguagem de Programação, começamos utilizando um interpretador interativo para testar os primeiros comandos da linguagem

→ Posteriormente, passamos a utilizar o editor de texto para desenvolver e salvar nossos programas em arquivos.

→ A estes arquivos, damos o nome de ->scripts<- .

Módulos

→ Conforme os projetos se tornam mais complexos, começa a ficar inviável utilizar um único arquivo para salvar todo o programa

→ Dividimos o script em vários arquivos para facilitar a organização e manutenção do código.

→ A estes arquivos, damos o nome de módulos

→ Não há diferença “prática” entre script e módulo

Pacotes

→ Conforme os projetos se tornam ainda mais complexos, podemos precisar de muitos arquivos (módulos);

→ Dividimos os módulos em pastas para, novamente, facilitar a organização e manutenção do código;

→ À estas pastas, damos o nome de pacotes.

Bibliotecas em python

→ Em Python, bibliotecas são coleções de módulos que contêm funcionalidades reutilizáveis;

→ Nas bibliotecas, os módulos geralmente são organizados em pacotes;

→ Há três tipos de bibliotecas:

    ↳ Integradas: math, datetime, ... ;

    ↳ De terceiros: geralmente instaladas via pip;

    ↳ Próprias;

Analisando os módulos


Listando módulos disponíveis no escopo:

>> dir()

>> import math

>> dir()

Obtendo o arquivo associado a um módulo:

>> import turtle

>> turtle.__file__

Analisando os módulos

→ Todo arquivo Python contendo definições e declarações é um módulo

→ O nome do módulo é o próprio nome do arquivo (sem a extensão .py)

→ Para obter o nome do módulo, utilizamos <modulo>.__name__

meu_modulo.py

>> import meu_modulo

>> meu_modulo.__name__

Executando módulos

→ Uma das formas para executar um módulo é com o comando python <nome do módulo>.py, com o botão “play” do VSCode ou com o F5 do IDLE

→ Ao importarmos um módulo, o interpretador do Python executa todo o seu conteúdo uma única vez

meu_modulo.py

print(
    f'Nome do módulo: 
    {__name__!r}'
)

>> import meu_modulo

→ Geralmente queremos importar os módulos para carregar suas funcionalidades e não executá-los como um todo

→ Interessante: quando um módulo é executado diretamente, ele recebe um nome especial:
    ↳ __main__

Ideia:

meu_modulo.py

def exibe_nome():
    print(f'Nome do módulo: {__name__!r}’)

if __name__ == '__main__’:
    exibe_nome()

Importando módulos

→ Quando usamos o comando import, o Python

    ↳ 1. verifica se aquele módulo já foi importado naquela sessão. Se sim, ele reutiliza a mesma referência para o módulo já existente em memória e interrompe o processo.

    ↳ 2. Se o módulo ainda não foi importado, o Python irá fazer uma busca a partir de uma lista de diretórios que pode ser vista na variável sys.path

→ Diretórios em que o Python faz a busca por módulos para importação:

>> import sys

>> sys.path

→ As bibliotecas instaladas vão para algum destes diretórios. Explore-os!


Importando módulos com apelidos

Podemos usar alias (apelidos) para módulos

>>import <nome do módulo> as <apelido>

Exemplo com NumPy:

>> import numpy

>>dir()

>> import numpy as np

>>dir()

Importando partes dos módulos

→ Podemos importar apenas a “parte” do módulo que será útil para o programa

>>from <nome do módulo> import <nome do elemento>

→ Exemplo com math:

>> from math import cos, pi, sin, tan

>> dir()

Organizando módulos em pacotes

→ Organizamos módulos em pastas (diretórios) que chamamos de pacotes

→ Em versões anteriores do Python, para que um diretório fosse realmente identificado como um pacote, era necessário incluir um arquivo especial chamado: 
    ↳ __init__.py

→ Este arquivo é opcional em versões mais recentes, mas ainda pode ser usado para inicializar módulos'''
'''
Exemplo:

imagem/
├── __init__.py
├── ajustes/
│   ├── __init__.py
│   ├── brilho.py
│   ├── contraste.py
│   ├── cor.py
│   ├── sepia.py
├── efeitos/
│   ├── __init__.py
│   ├── desfoque/
│   │   ├── __init__.py
│   │   ├── desfoque_gaussiano.py
│   │   ├── desfoque_movimento.py
│   │   ├── fragmentar.py
│   ├── estilizar/
│   │   ├── __init__.py
│   │   ├── bordas.py
│   │   ├── contorno.py
│   │   ├── relevo.py
│   ├── foto/
│       ├── __init__.py
│       ├── aumentar_nitidez.py
│       ├── reduzir_olho_vermelho.py
│       ├── suavizar.py
│       ├── vinheta.py
├── formatos/
│   ├── __init__.py
│   ├── bmp.py
│   ├── gif.py
│   ├── jpg.py
│   ├── png.py
│   ├── tiff.py
├── tela/
    ├── __init__.py
    ├── girar.py
    ├── inverter.py
    ├── redimensionar.py

'''

# %%
