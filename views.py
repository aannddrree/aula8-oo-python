class Motor:

    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao


class Carro:


    def __init__(self, nome, marca, motor):
        self.nome = nome
        self.marca = marca
        self.motor = motor

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

