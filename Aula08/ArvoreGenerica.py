
from No import No
class ArvoreGenerica():
    def __init__(self):
        self.raiz = None

    def adicionar_no(self, valor, valorPaiProcurado=None):
        novo_no = No(valor)

        if valorPaiProcurado is None:
            self.raiz = novo_no
        else:
            pai_atual = self.raiz
            pai_encontrado, _ = self.buscarNoAndPai(valorPaiProcurado, pai_atual)

            if pai_encontrado is None:
                input("Papai nao encontrado! Enter")
            else:
                pai_encontrado.adicionar_filho(novo_no)


    def buscarNoAndPai(self, valor, pai_atual=None, pai=None):
        if pai_atual is None:
            pai_atual = self.raiz
        
        if pai_atual.valor == valor:
            return pai_atual, pai

        for filho in pai_atual.filhos:
            resultado = self.buscarNoAndPai(valor, filho, pai_atual)
            if resultado != (None, None):
                return resultado
        
        return None, None

    def imprimir(self, prefixo="", ultimo=True):
        linha = "|___" if ultimo else "|---"
        print(prefixo + linha + str(nodo.valor))

        if ultimo:
            novo_prefixo = prefixo + "    "
        else:
            novo_prefixo = prefixo + "|   "

        contagem_filhos = len(nodo.filhos)
        for i, filho in enumerate(nodo.filhos):
            ultimo_filho = (i == contagem_filhos - 1)
            imprimir(filho, novo_prefixo, ultimo_filho)