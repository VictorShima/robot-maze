## Mapa
#
# O Mapa é responsável por gerir todo o desenho das unidades e da grelha
# de jogo.
#
# Ele contém um dict de associações entre Unidades e desenhos, e sempre
# que uma unidade mudar de estado é necessário pedir ao mapa para
# actualizar a unidade graficamente.
##

import cocos



class Mapa ( cocos.layer.Layer ) :




    margem = 30




    def __init__ ( self, linhas, colunas ) :
        super( Mapa, self ).__init__() # Necessario para desenhar o Layer
        self.linhas = linhas
        self.colunas = colunas
        # @TODO Montar chão e definir melhor onde as coisas sao desenhadas
        self.desenhos = {}




    # Insere uma unidade ao mapa para que o mapa seja capaz de desenhar
    # a imagem correspondente.
    def inserirUnidade ( self, unid ) :

        # De acordo com o tipo de unidade, o mapa desenha um sprite diferente
        ficheiro = '';
        if unid.tipo == 'robo' :
            ficheiro = 'codigo-inicial/robot-pixelart.png'
        elif unid.tipo == 'meta' :
            ficheiro = 'codigo-inicial/meta-pixelart.png'
        elif unid.tipo == 'pedra' :
            ficheiro = 'codigo-inicial/pedra-pixelart.png'
        elif unid.tipo == 'ponto' :
            ficheiro = 'codigo-inicial/ponto-pixelart.png'

        # Criar o sprite, adicionar ao Layer e fazer associação
        novoDesenho = cocos.sprite.Sprite( ficheiro )
        novoDesenho.position = self.calcularPosicaoNoEcra( unid.posicao )
        self.add( novoDesenho, z=3 )
        self.desenhos[ unid.id ] = novoDesenho




    # Pede ao mapa para actualizar (possivelmente) a posicão da unidade
    # na tela gráfica.
    def actualizarUnidade ( self, unid ) :
        des = self.desenhos[ unid.id ]
        if ( not des ) :
            return # @TODO Definir algum sistema de erros
        posicaoActual = self.calcularPosicaoNoEcra( unid.posicao )
        accaoMover = cocos.actions.MoveTo( posicaoActual, duration=0.5 )
        des.do( accaoMover )




    # Quando uma unidade é removida (por exemplo um ponto) então é
    # preciso retira-la do mapa.
    # @TODO
    def removerUnidade ( self, unid ) :
        return




    def calcularPosicaoNoEcra ( self, pos ) :
        return (
            pos[0] * 32 + Mapa.margem,
            pos[1] * 32 + Mapa.margem
        )
