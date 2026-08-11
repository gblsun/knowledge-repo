# Exercício

Crie um programa para gerenciar o acesso de usuários em uma plataforma. Este programa deve:
* Criar novos perfis: solicitar um nome de usuário e senha (a senha deve ser digitada duas vezes). Caso o nome não esteja sendo usado por outros usuários e as senhas estejam iguais, as credenciais do usuário devem ser salvas em um arquivo JSON. 
* Alterar senha: solicitar inicialmente o nome do usuário e a senha atual. Se o usuário estiver cadastrado e a senha estiver correta, deve então solicitar a nova senha (duas vezes) e alterá-la no arquivo JSON. A alteração deve ser registrada em um arquivo de texto, contendo o nome do usuário e o horário em que a alteração foi feita.
* Listar usuários e senhas: gerar uma planilha com os dados de usuário e senha e exportar para formato csv.

Obs:
~~~
3 funções e 1 programa principal
senhas.json
{
    ''vitor'':''123'',
    ''joao'':''234'',
    ''maria'':''456''
}
verifica se o arthur ja esta cadastrado
    se nao estiver cadastrado, faça registre o arthur

precisa de log de alteração de senhas
ou seja: log.txt
fulano alterou a senha em 25/10/2024 as 09:07
idem 
idem

listar-
pegar o arquivo json
fazer a conversão pra csv
exportar para uma planilha
~~~