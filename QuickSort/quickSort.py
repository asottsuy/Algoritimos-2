#LEFT = ponteiro que defino o primeiro elemento da lista
#RIGHT = ponteira que define o ultimo elemento da lista


#comeca pelo fim pois se trata de um algoritmo de recursao
def quickSort(list, left, right):
    if left < right: #se o primeiro element for maior q o ultimo encerra a funcao

                #partition
        pivo = definirPosicaoPivo(list, left, right) #define a posicao do pivo
        #a partir daqui o pivo está alinhado no centro
        #como o pivo é 'i', então tudo que estive a esquerda e o array menor q pivo e a direita maior.
        #então o ponteiro 'right' do primeiro array vai ser o antes do pivo
        #e o 'left' do array da direita vai ser o elemento depois do pivo

        quickSort(list, left, pivo-1) #lado esquerdo do array separado anteriormente
        quickSort(list, pivo+1, right) #lado direito do array separado anteriormente 
        #  o 4 é o p-1             o 7 é o p+1
        #   3 2 1 0 4       5      7 9 8 6
        #   l       r       p      l     r
        print(list)
    print(list)

#a funcao não divide litralmente em sub-arrays, apenas divide pela recursao,definidos pelos ponteiros.

def definirPosicaoPivo(list, left, right): #a funcao desse metodo é definir o lado esquerdo e o direto do array definindo o pivo no centro
    pivo = list[right] #diz q o pivo é o lado direito do arr
    print("Pivô: ", pivo)

    i = left - 1 #o 'i' aponta pro nada inicialmente
    #a var i vai ser responsavel por guardar o indice o qual o elemento que atender o a condição troquem de lugar

    for j in range(left, right):#iterar sobre o arr
        if list[j] <= pivo: #se o j for igual ou menor q o pivo
            i = i+1 #adiciona +1 ao 'i' 
        
            list[i], list[j] = list[j], list[i]#trocando o valor da posicao 'j' com o 'i'
            print("trocado ", list[j] ,"por ", list[i])
            print(list)

    list[i+1], list[right] = list[right], list[i+1] #trocamos de lugar o 'i' pelo pivo para deixar o pivo no centro do arr
    print(list)

    return i+1 #retorna por final a posicao do pivo no momento


