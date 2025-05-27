from Nodo import Nodo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def addInicio(self, valor):
        nodo = Nodo( valor )
        if self.inicio != None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimir()
        self.tamanho += 1

    def addFim(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()
        self.tamanho += 1

    def removerInicio(self):
        if self.inicio == None:
            print("Nenhum dado removido!")
        else:
            self.inicio = self.inicio.prox
        self.imprimir()
        self.tamanho -= 1
    
    def removerFim(self):
        if self.inicio == None:
            print("Nenhum dado removido!")
        elif self.inicio.prox == None:
            self.inicio = None
            self.tamanho -= 1
        else:
            anterior = self.inicio
            aux = self.inicio.prox
            while aux.prox:
                anterior = aux
                aux = aux.prox
            
            anterior.prox = None
            self.tamanho -= 1
        self.imprimir()

    def remover(self, valor):
        encontrou = False
        if self.inicio == None:
            print("A lista está vazia!")
        elif self.inicio.valor == valor:
            self.inicio = self.inicio.prox
            encontrou = True
        else:
            anterior = self.inicio
            aux = self.inicio.prox
            while aux:
                if aux.valor == valor:
                    anterior.prox = aux.prox
                    encontrou = True
                    break
                anterior = aux
                aux = aux.prox

            if not encontrou:
                print("\n-----------------------------")
                print(valor + " não encontrado") 
        self.imprimir()


    def imprimir(self):
        print("\n----------------------------------")
        if self.inicio == None:
            print( "\nLista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.valor )
                aux = aux.prox