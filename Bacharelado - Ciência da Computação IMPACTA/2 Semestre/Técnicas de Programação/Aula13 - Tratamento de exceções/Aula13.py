'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 11: técnicas de programação IMPACTA 19 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳

Tratamento
    de
        exceções

Como se proteger de erros em tempo de execução??


Exceções

Uma exceção é uma condição anormal que altera ou interrompe o fluxo de execução de um programa.

→ Possíveis causas:
    ↳ Erros de hardware;
    ↳ Erros de programação;
    ↳ o Erros de divisão por zero;
    ↳ o Acesso a variáveis nulas;
    ↳ Valores fora de faixa;
    ↳ o Erro na abertura de um arquivo (entrada/saída); 
    ↳ Falha na memória;

Exceções em python

→ A linguagem Python possui um mecanismo para o tratamento de exceções que podem ocorrer em tempo de execução do programa
    ↳ O surgimento de uma exceção ocasiona a interrupção imediata do programa. Porém, podemos tratá-las para evitar esta interrupção;
    ↳ O uso correto de exceções torna o programa mais robusto e confiável;
    ↳ Uso exagerado polui o código e torna o programa mais lento;

Error e Exception

----------> ERROR <---------- 
→ Error representa um problema grave, de difícil (ou impossível) recuperação;
→ Geralmente causam o encerramento do programa;
→ Não devem ser tratados durante a execução do programa;

→ Exemplos:
    ↳ Erros de sintaxe: devem ser corrigidos antes da execução do programa;
    ↳ Erros de semântica: utilizamos testes unitários para lidar com eles;

----------> EXCEPTION <----------
→ Exception são exceções que podem ser lançadas pelos métodos do Python ou pelo seu programa durante a execução;

→ Representam situações inesperadas, porém contornáveis;
→ Devem ser tratadas durante a execução do programa;

→ Existem duas situações: 

o levantamento e o 
tratamento de exceções;

-nome da classe representada em python?

Tratamento de excessões

→ Importante para garantir que a aplicação ou programa continue funcionando ao encontrar algo inesperado em relação ao seu funcionamento normal;
→ Permite criar desvios no fluxo do programa para que sejam tomadas as medidas necessárias:
    ↳ Enviar mensagens aos usuários;
    ↳ Escrever mensagens de log;
    ↳ Reagendar a tarefa que falhou;
    ↳ Fechar um arquivo aberto;
    ↳ Encerrar a conexão com o banco de dados;

→ O tratamento de exceções em Python é feito com o bloco try-except
    ↳Trecho de código do bloco try é executado;
    ↳Uma falha redireciona a execução para o bloco except e, posteriormente, o bloco finally (opcional) é executado;
    ↳Se não ocorrer falha, o bloco else (opcional) e, posteriormente, o bloco finally, são executados;


Importante para garantir que a aplicação ou programa continue funcionando ao encontrar algo inesperado em relação ao seu funcionamento normal
→ Permite criar desvios no fluxo do programa para que sejam tomadas as medidas necessárias:
    ↳ Enviar mensagens aos usuários;
    ↳ Escrever mensagens de log;
    ↳ Reagendar a tarefa que falhou;
    ↳ Fechar um arquivo aberto;
    ↳ Encerrar a conexão com o banco de dados;

→ O tratamento de exceções em Python é feito com o bloco try-except
    ↳ Trecho de código do bloco try é executado;
    ↳ Uma falha redireciona a execução para o bloco except e, posteriormente, o bloco finally (opcional) é executado;
    ↳ Se não ocorrer falha, o bloco else (opcional) e, posteriormente, o bloco finally, são executados.'''
# %% 
# try:
#     # código suscetível a falha
# except:
#     # código executado após ocorrer um erro
# else:
#     # código executado apenas se nenhum erro ocorrer
# finally:
#     # código executado sempre
# %%
# Trecho de código seguro
x = int(input())
y = int(input())

# Trecho de código susceptível a erro
try:
    z = x/y
except:
    print('Não é possível dividir por zero')
else:
    print(z)
finally:
    print('Programa Encerrado!')
# %%

'''
→ Um único bloco de código pode gerar diferentes tipos de falha
→ Utiliza-se múltiplos blocos except'''
# %%
# from paciente import Paciente, NameIsEmptyError 
# try:
#     nome = input('Digite o nome do paciente: ')
#     p = Paciente(nome)
# except TypeError:
#     print('O nome deve ser uma string')
# except NameIsEmptyError:
#     print('O nome não pode ser uma string vazia')
# except Exception as e:
#     print('Ocorreu um erro inesperado ao criar o objeto')
#     print('informações do erro:', e)
# %%

# %%
# Trecho de código seguro
x = int(input())
y = int(input())

# Trecho de código susceptível a erro
try:
    z = x/y
except Exception as e: #excessão genérica e
    print('Deu o seguinte erro:')
    print(e)
else:
    print(z)
finally:
    print('Programa Encerrado!')
# %%

'''
Lançando excessões

→ Também é possível lançar uma exceção em alguma situação específica, utilizando a palavra-chave raise
→ O comando raise é seguido do tipo de exceção que será gerada
→ Em Python, é possível lançar qualquer tipo de exceção
→ As exceções são organizadas em hierarquia


hierarquia de excessões:
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

→ Exemplo: '''
# %%
def incrementa_int(n):
    if not isinstance(n, int):
        raise TypeError('n deve ser um inteiro')
    return n + 1

# isinstance: serve para saber qual o tipo da variável.
# raise (levantar), ou seja: levantar uma excessão.
# %%

# %%
# Trecho de código seguro
x = int(input())
y = int(input())

# Trecho de código susceptível a erro
if y==0:
    raise TypeError('Não pode ser dividido por zero.')
# %%
'''
Propagação de exceções

→ Caso um tratador adequado não seja encontrado
no bloco onde a exceção foi lançada, ela é
propagada para o nível mais externo
→ A propagação irá continuar até que algum tratador
seja encontrado ou até chegar ao nível do
interpretador
→ O tratamento padrão do interpretador é imprimir a
exceção na saída padrão e finalizar o programa'''
# %%
def incrementa_int(n):
    if not isinstance(n, int):
        raise TypeError('n deve ser um inteiro')
    return n + 1

def calcula_idade(idade):
    nova_idade = incrementa_int(idade)
    print('esse código não é executado se der erro na linha acima')
    return nova_idade

def main():
    print('executando a função principal...')
    resposta = calcula_idade(20.5)
    print('esse código não será executado se der erro na linha acima')
    print('a nova idade é:', resposta)
    
if __name__ == '__main__':
    print('chamando a função principal')
    main()
    print('esse código não será executado se der erro na linha acima')
# %%
'''
Criando exceções

→ Além de usar as exceções embutidas do Python, o programador pode criar suas próprias exceções
→ Basta criar uma classe que esteja na hierarquia abaixo de Exception
→ Coloque como propriedades da exceção informações importantes do contexto no qual ela foi lançada.

→ Exemplo:sistema de cadastro para clínica
veterinária.
→ Nova funcionalidade: criar a ficha dos animais:
    ↳ Classe Paciente;
    ↳ Campos preenchidos incorretamente (ex. nome do paciente em branco) geram uma exceção.'''
# %%
class NameIsEmptyError(Exception): 
    pass
# %%
'''
Exemplo: sistema de cadastro para clínica veterinária.''' 
# %%
class Paciente:
    def __init__(self, nome):
        if not isinstance(nome, str):
            raise TypeError("'nome' inválido")
        if nome == '':
            raise NameIsEmptyError("'nome' é obrigatório")
        self.nome = nome 
# %%
