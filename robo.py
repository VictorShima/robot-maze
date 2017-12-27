## Robo
#
# ATENÇÃO: Isto é um exemplo de uma sub-classe de unidade.
#          Este código não é usado no programa, mas seria possível
#          criar uma subclasse para cada tipo de Unidade se quisermos
#          começar a criar funcionalidades diferentes. Porém, neste
#          projecto estamos a delegar todas as regras para o jogo, que
#          serve de livro de regras.
#          Não cheguei a definir subclasses porque actualmente não daria
#          para ver as vantagens disto.
##


from unidade import Unidade


class Robo ( Unidade ) :


    def __init__ ( self, posicao ) :
        super( Robo, self ).__init__( 'robo', posicao )
