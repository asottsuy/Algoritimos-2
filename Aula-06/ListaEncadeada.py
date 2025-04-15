from No import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def addInicio(self, valor):
        nodo = No( valor )
        if self.inicio != None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.tamanho += 1
        self.imprimir()


    def imprimir(self):
        print("\n----------------------------------")
        if self.inicio == None:
            print( "\nLista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox