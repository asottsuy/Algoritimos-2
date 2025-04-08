from ListaEncadeada import ListaEncadeada

class Bubble:
    def __init__(self, ListaEncadeada):
        self.lista = ListaEncadeada
        

    def ordenarLista(self):
        if self.lista.tamanho <= 1:
            return  

        for i in range (self.lista.tamanho): #percorre pelo tamanho da lista
            no_atual = self.lista.inicio #define o no atual
            no_ante = None
            for j in range(self.lista.tamanho - i - 1): #pecorre pelos elementos da lista - indice -1
                if no_atual.valor > no_atual.prox.valor:
                    aux = no_atual.prox
                    no_atual.prox = aux.prox
                    aux.prox = no_atual

                    if no_ante is not None:
                        no_ante.prox = aux
                    else:
                        self.lista.inicio = aux

                    no_ante = aux
                    
                else:
                    no_ante = no_atual

                no_atual = no_atual.prox
                    
        return self.lista


    
lista = ListaEncadeada()
lista.adicionar('D')
lista.adicionar('A')
lista.adicionar('F')
lista.adicionar('E')
lista.adicionar('B')
lista.adicionar('C')

print("antes")
lista.imprimir()

bubble = Bubble(lista)
bubble.ordenarLista()

print("depois")
lista.imprimir()