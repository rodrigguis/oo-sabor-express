"""Modulo modelos"""

from modelos.avaliacao import Avaliacao

class Restaurante:
    """Class representation Restaurant"""

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar(cls):
        """Method for list restaurants"""
        cabecalho_nome = 'Nome Restaurante'.ljust(25)
        cabecalho_categoria = 'Categoria'.ljust(10)
        cabecalho_avaliacao = 'Avaliacao'.ljust(25)

        print(f'''
            {cabecalho_nome} | {cabecalho_categoria} | 
            {cabecalho_avaliacao} | Status
        ''')
        for restaurante in cls.restaurantes:
            print(f'''
                {restaurante.nome.ljust(20)} | 
                {restaurante.categoria.upper().ljust(10)} | 
                {str(restaurante.media_avaliacoes).ljust(25)} | 
                {restaurante.ativo}
            ''')

    @property
    def ativo(self):
        """Method for update status"""
        return '☑' if self._ativo else '☒'

    def alternar_estado(self):
        """Method for alter status"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Method for reception avaliation"""
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Method for average avaliations"""
        if not self._avaliacao:
            return '-'

        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)

        return media
