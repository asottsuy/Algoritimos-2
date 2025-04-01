from Nodo import Nodo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = Nodo(valor)
        if self.inicio is None:
            self.inicio = no
            self.tamanho += 1
        else:
            aux = no
            while aux.prox is not None:
                aux.prox = no
                self.tamanho += 1
                print(aux.valor)
        
    

lista = ListaEncadeada()
lista.adicionar(3)
lista.adicionar(32)
lista.adicionar(1)
                
                

            


        
