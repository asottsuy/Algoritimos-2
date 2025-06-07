class No:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

            
    def adicionar_filho_left(self, filho):
        self.left = filho
        
    def adicionar_filho_right(self, filho):
        self.right = filho
    
    def __str__(self):
        return str(self.valor)