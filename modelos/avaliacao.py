""" Modulo modelos """

class Avaliacao:
    """Class represent Avaliation"""

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    def show_nota(self):
        """Method show nota"""
        return self._nota

    def show_cliente(self):
        """Method show client Avaliation"""
        return self._cliente
