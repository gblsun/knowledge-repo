from benchmark import *
from primo import *

funcoes = [primo1, primo2, primo3, primo4, primo5, primo6, primo7]

numeros = [1000000, 1000003, 1000000000, 1000000007]

func_dict = {}
for funcao in funcoes:
    print('---'+funcao.__name__,'---')
    num_dict = {}
    for num in numeros:
        
        res = tempo(funcao,num)
        print(f"n = {num}. tempo = {res}")
        num_dict[num] = res
    func_dict[funcao.__name__] = num_dict

print(func_dict)