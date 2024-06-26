""" Modulo modelos """


class Musica:
    """Class represent Music"""

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} {self.artista} {self.duracao}'

    def show_musica(self):
        """Method show nota"""
        musica1 = Musica(nome='Under Pressure', artista='Queen', duracao=248)
        print(f'Dados: {musica1.nome}, artista: {musica1.artista} duracao: {musica1.duracao}')
