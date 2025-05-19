from quickSort import quickSort, definirPosicaoPivo

lista = [9,4,3,8,2,7,0,6,1,5]


print("Lista NÂO ordenada: ",lista,"\n===========================")
quickSort(lista, 0, len(lista)-1 )


print("Lista Ordenada: ", lista)