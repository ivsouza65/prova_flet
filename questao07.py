class Carro:
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca