def busca_binaria(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return True
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

def busca_binaria_recursiva(lista, valor):
    if len(lista)==0:
        return False
    
    inicio = 0
    fim = len(lista)-1
    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return True
    elif lista[meio] < valor:
        return busca_binaria(lista[meio+1:], valor)
    else:
        return busca_binaria(lista[:meio-1], valor)
