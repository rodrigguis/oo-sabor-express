class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen', duracao=248)
print(f'Dados musica nome: {musica1.nome}, artista: {musica1.artista} e duracao: {musica1.duracao}')