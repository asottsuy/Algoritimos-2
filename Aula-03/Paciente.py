class Paciente:
    def __init__(self, nome, idade, numero):
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.prox =  None
    
    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} Numero: {self.numero}"

    
