from Bubble import Bubble
from ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()
lista.addInicio("F")
lista.addInicio("D")
lista.addInicio("R")
lista.addInicio("G")
lista.addInicio("A")
lista.addInicio("B")

lista_ordenada = Bubble(lista)
lista_ordenada.ordenarLista()

lista_ordenada.imprimir()
