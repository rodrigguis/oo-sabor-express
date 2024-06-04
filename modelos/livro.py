""" Modulo modelos """


class Livro:
    """ Class represent a Livro """

    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self) -> str:
        return f'{self.titulo} por {self.autor} - {self.paginas} paginas'

    @property
    def titulo_autor(self):
        """
        Property title autor
        """
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        """Function increment pages"""
        self.paginas += quantidade
