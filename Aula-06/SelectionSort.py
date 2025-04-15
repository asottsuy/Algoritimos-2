from ListaEncadeada import ListaEncadeada

class SelectionSort():
    def __init__(self, ListaEncadeada):
        self.lista = ListaEncadeada

    def selection_sort(self):
        if self.lista.inicio is None: #verificar se a lista nao esta vazia
            return self.lista
        no_atual = self.lista.inicio
        for i in range(self.lista.tamanho): #vai iterar pelo tamanho da lista
            menor_n = no_atual  #define que o menor numero no momento e o elemento atual
            aux = no_atual.prox
            for j in range(i + 1, self.lista.tamanho): #vai iterar novamente comecando pelo elemento atual + 1, até o tamanho total da lista
                if no_atual.dado < aux.dado : #se lista no indice j for maior que lista no indice do menor numero atual
                    aux = no_atual.prox
                    no_atual.prox = aux.prox
                    no_atual = aux
                    aux = aux.prox
            #depois de percorrer todos os elementos vai atualizar os dados para preparar a prox iteracao
            #self.lista[i], self.lista[min_i] = self.lista[min_i], self.lista[i]
            menor_n, no_atual = no_atual, menor_n
            #lista no indice atual = lista no indice do menor numero atual
            #lista no indice do menor numero atual = lista no indice atual
        self.lista.imprimir()
