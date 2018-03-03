## Unidade
#
# Propriedades comuns a todas as unidades.
##


import cocos



## Unidade
#
# Unidades são objectos que estão no mapa. Todas as unidades têm um
# tipo e a posição onde elas estão.
##
class Unidade () :




    # Cada unidade recebe um novo numero quando é gerada.
    proximoId = 1




    # @param tipo {string} Nome da unidade
    # @param posicao {2-tuple-of-int} Posicao da unidade no mapa
    def __init__ ( self, tipo, posicao ) :
        self.id = Unidade.proximoId
        Unidade.proximoId += 1
        self.tipo = tipo
        self.posicao = posicao
