from Paciente import Paciente

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def queue(self, nome, idade, numero):
        paciente = Paciente(nome, idade, numero)
        aux = self.inicio

        if self.inicio == None: #se a lista for vazia
            self.inicio = paciente
            self.fim = paciente
        else:
            while aux.prox is not None:
                aux = aux.prox

            aux.prox = paciente
            paciente.prox = None
        
        self.tamanho += 1
        self.imprimir()
        

    def imprimir(self):
        print("\n=========================")
        if self.inicio == None:
            print("Fila vazia!")
        else:
            aux = self.inicio
            while aux is not None:
                print (aux)
                aux = aux.prox
            print(f"Tamanho da Fila: {self.tamanho}")
    
    def imprimir_numero(self, numero):
        print("\n=========================")
        if self.inicio == None:
            print("Fila vazia!")
        else:
            aux = self.inicio
            while aux.numero != numero:
                aux = aux.prox
            print(aux)