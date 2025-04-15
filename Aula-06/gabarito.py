def selection_sort(lista):
    if not lista:
        return lista
    for i in range(len(lista)):
        min_i = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]

    print(lista)


selection_sort([2, 4, 3, 6, 9, 1, 6, 3])