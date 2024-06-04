''' Modulos modelos '''

from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 0)
restaurante_praca.receber_avaliacao('Tan', 0)
restaurante_praca.receber_avaliacao('Rob', 0)

def main():
    '''
    Principal class
    '''
    Restaurante.listar()

if __name__ == '__main__':
    main()
