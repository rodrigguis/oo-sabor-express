''' Modulo modelos '''

class Livro:
    ''' Class represent a Livro '''

    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self) -> str:
        return f'{self.titulo} por {self.autor} - {self.paginas} paginas'

    @property
    def titulo_autor(self):
        '''
        Property title autor
        '''
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        '''Function increment pages'''
        self.paginas += quantidade

livro_aventura = Livro('Coraline', 'Dona Mata', 350)
print(f'O livro {livro_aventura.titulo}, da autora {livro_aventura.autor} tem {livro_aventura.paginas} paginas')

livro_aventura.aumentar_paginas(10)
print(f'A quantidade de paginas do livro foi alterada para: {livro_aventura.paginas}')

livro_aventura.autor = 'Renato'
print(f'O autor foi alterado incorretamente para: {livro_aventura.autor}')
