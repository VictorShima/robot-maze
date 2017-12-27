## Painel
#
# O Painel vai conter o HUD do jogo. Por enquanto é a pontuação.
##


import cocos




class Painel ( cocos.layer.Layer ) :




    def __init__ ( self ) :
        super( Painel, self ).__init__() # Dessenhar a layer
        self.pontuacao = cocos.text.Label(
            'Pontos: 0',
            font_size=14,
            x=30,
            y=350
        )
        self.add( self.pontuacao )




    def actualizarPontuacao ( pontuacao ) :
        self.pontuacao.element.text = 'Pontos: ' + pontuacao
