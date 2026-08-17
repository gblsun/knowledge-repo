# 3 situações
# REP -> Média < 5 || 10 ou + faltas
# REC -> Média >= 5 e  < 7 || Menos de 10 faltas
# AP -> Média >= 7 || Menos de 10 faltas 

nome = input("Digite o nome do aluno: ")
faltas = int(input("Digite a quantidade de faltas: "))
ap1 = float(input("Digite a nota da AP1: "))
ap2 = float(input("Digite a nota da AP2: "))
media = (ap1+ap2)/2

if media < 5 or faltas>=10:
    print(nome,"você teve: ",faltas,"e média",media)
    print("De acordo com o regulamento da IMPACTA, você foi reprovado por nota e/ou quantidades de falta")
elif (media >= 5 and media<7) and faltas<10:
    print(nome,"Não desanime. Com ",media," ainda há esperança")
else:
    print("PARABÉNS,",nome,"você É FERA!!!. Feshow com: ",media)