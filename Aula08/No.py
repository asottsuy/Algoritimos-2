class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)
        

    def percorrer(self):
        print(self.valor)
        for filho in self.filhos:
            filho.percorrer()
    
    def buscar(self, valor):
        if self.valor == valor:
            #final  muito feliz por n precisa percorrer a lista
            return self
        for filho in self.filhos:
            resultado = filho.buscar(valor)
            if resultado:
                #final feliz caso o valor seja encontrado
                return resultado
        #caso o valor nao exista
        return None
            

    