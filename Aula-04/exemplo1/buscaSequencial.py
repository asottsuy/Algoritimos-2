lista = [1,41,54,66,12,21,5,2,49,99]

def buscaSequencial (lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            print(">", lista)
    print(lista)

busca = buscaSequencial(lista)
print(busca)
         