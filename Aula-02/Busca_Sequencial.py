import random
import Estrutura_Linear as el

"""f
Crie uma função que receba como parâmetros uma lista e a informação a ser encontrada
    nesta lista.
Esta função deverá retornar a posição da lista onde a informação foi encontrada,
    ou retornar None, caso a informação não seja encontrada.
"""

def buscaSequencial(lista, elemento):
    for i, num in enumerate(lista):
        print(elemento, num)
        if num == elemento:
            return print(f"Indice {i}\nNumero {num}")
    return None
    
lista_n_ordenada = el.dadosLineares(10,50)
print(buscaSequencial(lista_n_ordenada, random.choice(lista_n_ordenada) ))