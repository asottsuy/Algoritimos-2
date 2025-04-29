def ordena(vet_desordenado):
    max_val = max(vet_desordenado) #armazena o maior numero do vetor
    vet_auxiliar = [0] * (max_val + 1) #cria um array com max_val + 1 zeros(16)
    for num in vet_desordenado: #iterar a quantidade de elementos no vetor
        vet_auxiliar[num] += 1 #vai dizer que o numero 1 adicionado a ele mesmo vai ficar no indice num
    #aqui temos um vet_auxiliar com 15 posicoes com a quantidade de vezes que um valor aparece no vetor, na sua respectiva posicao (valor).

    for i in range(1, len(vet_auxiliar)): #iterar pelo tamanho de vet_aux(15)
        vet_auxiliar[i] += vet_auxiliar[i - 1] 
    vet_ordenado = [0] * len(vet_desordenado)
    for num in vet_desordenado:
        vet_ordenado[vet_auxiliar[num] - 1] = num
        vet_auxiliar[num] -= 1
    return vet_ordenado

array_desordenado = [7, 3, 3, 15, 4, 4, 2]
array_ordenado = ordena(array_desordenado)
print(array_ordenado)