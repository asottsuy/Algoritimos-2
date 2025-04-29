def ordena(vet_desordenado):
    max_val = max(vet_desordenado) #armazena o maior numero do vetor
    vet_auxiliar = [0] * (max_val + 1) #vet-aux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in vet_desordenado: #vet_desordenado = [7, 3, 3, 15, 4, 4, 2]
        vet_auxiliar[num] += 1 #vai dizer que o numero 1 adicionado a ele mesmo vai ficar no indice num
    #aqui temos um vet_auxiliar com 15 posicoes com a quantidade de vezes que um valor aparece no vetor, na sua respectiva posicao (valor).

    for i in range(1, len(vet_auxiliar)): #vet_aux = [0, 0, 1, 2, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
        vet_auxiliar[i] += vet_auxiliar[i - 1] #vet_aux = [0, 0, 1, 3, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7]
    vet_ordenado = [0] * len(vet_desordenado) #vet_ordenado = [0, 0, 0, 0, 0, 0, 0]
    for num in vet_desordenado: # num vai ser o elemento atual # vet_des = [7, 3, 3, 15, 4, 4, 2]
        vet_ordenado[vet_auxiliar[num] - 1] = num
        vet_auxiliar[num] -= 1
    return vet_ordenado

array_desordenado = [7, 3, 3, 15, 4, 4, 2]
array_ordenado = ordena(array_desordenado)
print(array_ordenado)