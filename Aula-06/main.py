from ListaEncadeada import ListaEncadeada
from SelectionSort import SelectionSort

lista = ListaEncadeada()
lista.addInicio(2)
lista.addInicio(4)
lista.addInicio(3)
lista.addInicio(6)
lista.addInicio(9)
lista.addInicio(1)
lista.addInicio(6)
lista.addInicio(3)

print(f"\nCheguei aqui Tamanho: {lista.tamanho}")

listaOrdenada = SelectionSort(lista)
listaOrdenada.selection_sort()

