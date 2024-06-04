from modelos.avaliacao import Avaliacao

class Restaurante: 
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
        print(f'{'Nome Restaurante'.ljust(20)} | {'Categoria'.ljust(10)} | {'Avaliacao'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(10)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self): 
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self): 
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota): 
        if 0 < nota <=5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self): 
        if not self._avaliacao: 
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)

        return media

