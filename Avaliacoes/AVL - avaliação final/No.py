class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1 #diferença da árvore binária comum

    def __str__(self):
        return f"End de memória: {hex(id(self))}\nL.Esq: {self.esquerda.valor}\nValor: {self.valor}\nL.Dir: {self.direita.valor}"
                
        
