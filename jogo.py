## Jogo
#
# É o gestor de todas as entidades.
# O Jogo:
#   - inicia o Inicializador,
#   - guarda todo o estado de jogo,
#   - comunica com o Mapa e com a Interface para desenhar,
#   - contém todas as regras de jogo.
##


import cocos
import random

from mapa import Mapa
from teclado import Teclado
from painel import Painel
from unidade import Unidade




class Jogo ( cocos.scene.Scene ):




    def __init__ ( self ) :
        super( Jogo, self ).__init__()

        self.estado = {
            'linhas' : 0,
            'colunas' : 0,
            'pontuacao': 0,
            'robo': None,
            'meta': None,
            'pedras': [],
            'pontos': []
        }
        self.inicializarEstado()

        self.teclado = None
        self.inicializarTeclado()

        self.mapa = None
        self.inicializarMapa()

        self.painel = None
        self.inicializarPainel()




    # O Estado vem todo a partir de um ficheiro de inicialização.
    def inicializarEstado ( self ) :

        # Vai abrir a ficheiro  'informacao_inicial.txt' e dividir o
        # conteúdo em vários pedaços de texto.
        file = open("info-inicial.txt", "r")
        content = file.read()
        tokens = content.split()

        # Extrair o tamanho do mapa.
        self.estado['linhas'] = int( tokens[0] )
        self.estado['colunas'] = int( tokens[1] )

        # Extrair a posição do robo
        xRobo = int( tokens[2] )
        yRobo = int( tokens[3] )
        self.robo = Unidade( 'robo', (xRobo,yRobo) )

        # Extrair a posição da meta
        xMeta = int( tokens[4] )
        yMeta = int( tokens[5] )
        self.meta = Unidade( 'meta', (xRobo,xMeta) )

        # Extrair a quantidade de pedras e posiciona-las.
        # @TODO: Ainda pode gerar por cima do robo ou outras unidades.
        numeroPedras = int( tokens[6] )
        for l in range( 1, numeroPedras + 1 ) :
            xPedra = random.randint( 1, self.estado['linhas'] )
            yPedra = random.randint( 1, self.estado['colunas'] )
            novaPedra = Unidade( 'pedra', (xPedra,yPedra) )
            self.estado['pedras'].append( novaPedra )

        # Extrair a quantidade de pontos e posiciona-las.
        # @TODO: Ainda pode gerar por cima do robo ou outras unidades.
        numeroPontos = int( tokens[7] )
        for l in range( 1, numeroPontos + 1 ) :
            xPonto = random.randint( 1, self.estado['linhas'] )
            yPonto = random.randint( 1, self.estado['colunas'] )
            novoPonto = Unidade( 'ponto', (xPonto,yPonto) )
            self.estado['pontos'].append( novoPonto )





    def inicializarTeclado ( self ) :
        self.teclado = Teclado ( self )
        self.add( self.teclado )




    def inicializarMapa ( self ) :
        self.mapa = Mapa( self.estado['linhas'], self.estado['colunas'] )

        # Temos que adicionar todas as unidades ao mapa, para que ele
        # as possa desenhar
        self.mapa.inserirUnidade( self.robo )
        self.mapa.inserirUnidade( self.meta )
        for p in self.estado['pedras'] :
            self.mapa.inserirUnidade( p )
        for p in self.estado['pontos'] :
            self.mapa.inserirUnidade( p )

        # Por final é preciso adicionar o mapa ao cenário do Jogo, para
        # que o jogo decidir desenhar o mapa.
        self.add( self.mapa )




    def inicializarPainel ( self ) :
        self.painel = Painel()
        self.add( self.painel )




    # Move o robo e executa o método de actualizão.
    def moverRobo ( self, movimento ) :
        posicaoDesejada = (
            self.robo.posicao[0] + movimento[0],
            self.robo.posicao[1] + movimento[1]
        )
        if ( self.podeMover( posicaoDesejada ) ) :
            self.robo.posicao = posicaoDesejada
            # É necessário actualizar sempre a unidade no mapa
            # depois de mexer nela.
            self.mapa.actualizarUnidade( self.robo )
            self.aposMover()




    # Verifica se o robo se pode mover para a posicaoDesejada.
    # Aqui é importante ver se um robo pode mover para cima de
    # uma pedra ou assim.
    def podeMover ( self, posicaoDesejada ) :
        # @TODO preencher
        return True




    # Esta função faz acontecer coisas depois do movimento do
    # robo. Por exemplo, as coisas que acontecem quando um robo
    # está por cima de uma moeda ou de uma meta.
    def aposMover ( self ) :
        # @TODO preencher
        return
