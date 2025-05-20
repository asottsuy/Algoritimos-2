from No import No

class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def adicionar_no(self, valor, pai=None):
        novo_no = No(valor)
        #preciso saber quem o pai, e o valor dele
        if self.raiz is None:
            self.raiz = novo_no
            return
        
        #quem e o pai?
        if pai is None:
            print("Erro, n tem pai")
            return
    
        no_pai = self.raiz.buscar(pai)
        if no_pai:
            no_pai.adicionar_filho(novo_no)
        else:
        print(f"Pai '{pai}'não encontrado na árvore")
            

    def imprimir(self):
        if self.raiz is None:
            print("Árvore vazia")

        
        
        

        
        