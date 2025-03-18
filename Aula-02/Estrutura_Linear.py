import random

def dadosLineares(qtdElementos, ValorMax) -> list:
    lista = []
    while len(lista) < qtdElementos:
        lista.append(random.randint(-1, ValorMax))
    return lista 

print(dadosLineares(10, 50))
        