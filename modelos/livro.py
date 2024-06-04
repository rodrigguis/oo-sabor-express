class Livro: 
    def __init__(self, titulo='', autor='', paginas=0):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas

    def __str__(self) -> str:
        return f'{self._titulo} por {self._autor} - {self._paginas} paginas'
    
    @property
    def titulo_autor(self): 
        return f'{self._titulo} por {self._autor}'
    
    def aumentar_paginas(self, quantidade): 
        self._paginas += quantidade

livro_aventura = Livro('Coraline', 'Dona Mata', 350)
print(f'O livro {livro_aventura._titulo}, da autora {livro_aventura._autor} tem {livro_aventura._paginas} paginas')

livro_aventura.aumentar_paginas(10)
print(f'A quantidade de paginas do livro foi alterada para: {livro_aventura._paginas}')

livro_aventura._autor = 'Renato'
print(f'O autor foi alterado incorretamente para: {livro_aventura._autor}')